import time
import logging
import numpy as np
from application.pipelines.hailo_whisper_pipeline import HailoWhisperPipeline
from application.utils.audio_utils import AudioUtils
from application.utils.record_utils import RecordUtils
from infrastructure.common_functions.postprocessing import clean_transcription
from infrastructure.common_functions.preprocessing import improve_input_audio, preprocess

system_logger = logging.getLogger(__name__)

class TranscribeAudioUseCase:
    def __init__(
            self,
            audio_utils: AudioUtils,
            record_utils: RecordUtils,
            whisper_hailo: HailoWhisperPipeline
    ):
        self.audio_utils = audio_utils
        self.record_utils = record_utils
        self.is_nhwc = True
        self.variant = "tiny"
        self.chunk_length = 10 if self.variant == "tiny" else 5
        self.whisper_hailo = whisper_hailo


    async def execute(self, audio_path: str):
        sampled_audio = self.audio_utils.load_audio(audio_path)

        sampled_audio, start_time = improve_input_audio(sampled_audio, vad=True)
        chunk_offset = start_time - 0.2
        if chunk_offset < 0:
            chunk_offset = 0

        mel_spectrograms = preprocess(
            sampled_audio,
            is_nhwc=self.is_nhwc,
            chunk_length=self.chunk_length,
            chunk_offset=chunk_offset
        )

        for mel in mel_spectrograms:
            # expected = self.whisper_hailo.encoder.input_layer.size  
            actual = mel.nbytes
            system_logger.debug(f"buffer size: actual={actual}")
            # mel = mel.astype(np.float32, copy=False)  # на случай float64
            # print("mel shape:", mel.shape, "dtype:", mel.dtype)
            # print("C_CONTIGUOUS:", mel.flags['C_CONTIGUOUS'], "shape:", mel.shape)
            # mel = mel.squeeze()
            # mel = mel.reshape(1, *mel.shape)    
            # mel = mel.transpose(0, 2, 1)             # (1, 80, 1000)
            # mel = mel.reshape(1, 1, 1000, 80)        # (NHWC)
            try:
                self.whisper_hailo.send_data(mel)
            except Exception as e:
                print(f"[ERROR] Failed to send data: {e}")
                return 
            time.sleep(0.2)
            transcription = clean_transcription(self.whisper_hailo.get_transcription())
            print(f"\n{transcription}")
            break

        return True

        # if args.reuse_audio:
        #     break  # Exit the loop if reusing audio

