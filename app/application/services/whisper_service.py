from application.pipelines.hailo_whisper_pipeline import HailoWhisperPipeline
from application.use_cases.transcribe_audio_use_case import TranscribeAudioUseCase
from application.utils.audio_utils import AudioUtils
from application.utils.record_utils import RecordUtils


class WhisperService:
    def __init__(
            self,
            audio_utils: AudioUtils,
            record_utils: RecordUtils,
            whisper_hailo: HailoWhisperPipeline,
    ):
        self.transcribe_audio_use_case = TranscribeAudioUseCase(
            audio_utils=audio_utils,
            record_utils=record_utils,
            whisper_hailo=whisper_hailo
        )

    async def transcribe_audio(self, audio_file_path: str):
        await self.transcribe_audio_use_case.execute(audio_path=audio_file_path)