"""Event handler for clients of the server."""
import argparse
import asyncio
import logging
import os
import tempfile
import wave
from typing import Optional

from wyoming.asr import Transcribe, Transcript
from wyoming.audio import AudioChunk, AudioStop
from wyoming.event import Event
from wyoming.info import Describe, Info
from wyoming.server import AsyncEventHandler

from infrastructure.config.services_config import get_whisper_service
from infrastructure.config.whisper_hailo import get_whisper_hailo

system_logger = logging.getLogger(__name__)


class WhisperHailoEventHandler(AsyncEventHandler):
    """Event handler for clients."""

    def __init__(
        self,
        wyoming_info: Info,
        *args,
        **kwargs,
    ) -> None:
        super().__init__(*args, **kwargs)

        self.wyoming_info_event = wyoming_info.event()
        self._wav_dir = tempfile.TemporaryDirectory()
        self._wav_path = os.path.join(self._wav_dir.name, "speech.wav")
        self._wav_file: Optional[wave.Wave_write] = None

        self.whisper_service = get_whisper_service()

    async def handle_event(self, event: Event) -> bool:
        if AudioChunk.is_type(event.type):
            chunk = AudioChunk.from_event(event)

            if self._wav_file is None:
                self._wav_file = wave.open(self._wav_path, "wb")
                self._wav_file.setframerate(chunk.rate)
                self._wav_file.setsampwidth(chunk.width)
                self._wav_file.setnchannels(chunk.channels)

            self._wav_file.writeframes(chunk.audio)
            return True

        if AudioStop.is_type(event.type):
            system_logger.debug("Audio stopped. Transcribing")
            assert self._wav_file is not None

            self._wav_file.close()
            self._wav_file = None

            whisper_hailo = get_whisper_hailo()

            try:
                result = await self.whisper_service.transcribe_audio(whisper_hailo, audio_file_path=self._wav_path)
            except Exception as e:
                system_logger.error(f"Error during transcription: {e}")
                return False
            finally:
                whisper_hailo.stop()

            await self.write_event(Transcript(text=result).event())
            system_logger.info(f"Successful transcription: {result}")

            return False
        
        if Transcribe.is_type(event.type):
            transcribe = Transcribe.from_event(event)
            if transcribe.language:
                system_logger.debug("Language set to %s", transcribe.language)
            return True

        if Describe.is_type(event.type):
            await self.write_event(self.wyoming_info_event)
            system_logger.debug("Sent info")
            return True

        return True