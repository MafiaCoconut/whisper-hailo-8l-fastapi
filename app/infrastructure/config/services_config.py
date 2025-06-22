from application.services.whisper_service import WhisperService
from infrastructure.config.utils_config import audio_utils, record_utils
from infrastructure.config.whisper_hailo import whisper_hailo


def get_whisper_service() -> WhisperService:
    return WhisperService(
        audio_utils=audio_utils,
        record_utils=record_utils,
        whisper_hailo=whisper_hailo,
    )