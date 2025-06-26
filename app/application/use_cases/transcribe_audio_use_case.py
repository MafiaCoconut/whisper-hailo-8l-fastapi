import os
import time
import logging
import numpy as np
from application.pipelines.hailo_whisper_pipeline import HailoWhisperPipeline
from application.utils.audio_utils import AudioUtils
from infrastructure.common_functions.postprocessing import clean_transcription
from infrastructure.common_functions.preprocessing import improve_input_audio, preprocess

system_logger = logging.getLogger(__name__)

class TranscribeAudioUseCase:
    def __init__(
            self,
            audio_utils: AudioUtils,
            # whisper_hailo: HailoWhisperPipeline
    ):
        self.audio_utils = audio_utils
        self.is_nhwc = True
        self.variant = "tiny"
        self.chunk_length = 10 if self.variant == "tiny" else 5
        # self.whisper_hailo = whisper_hailo


    async def execute(self, whisper_hailo, audio_path: str) -> str:
        print(f"IS_HAILO_ON_DEVICE: {os.getenv('IS_HAILO_ON_DEVICE')}")
        if os.getenv("IS_HAILO_ON_DEVICE") == 'TRUE':
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

            result = ""
            for mel in mel_spectrograms:
                whisper_hailo.send_data(mel)
                time.sleep(0.2)
                result += clean_transcription(whisper_hailo.get_transcription())
                break

            return result
        else:
            return "The recording cannot be decrypted due to the fact that there is no Hailo on this device"