import os
import logging
from fastapi import APIRouter, Response, FastAPI, Request, BackgroundTasks, UploadFile, File
from fastapi.params import Depends
from tempfile import NamedTemporaryFile
from infrastructure.config.whisper_hailo import get_whisper_hailo

from icecream import ic

from application.services.whisper_service import WhisperService
from infrastructure.config.services_config import get_whisper_service

router = APIRouter()

system_logger = logging.getLogger(__name__)
def config(app: FastAPI):
    app.include_router(router)


@router.post("/transcribe")
async def transcribe_audio(
        response: Response, background_tasks: BackgroundTasks,
        request: Request,
        file: UploadFile = File(...),
        whisper_service: WhisperService = Depends(get_whisper_service)):
    suffix = os.path.splitext(file.filename)[1]
    with NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        content = await file.read()
        tmp.write(content)
        tmp_path = tmp.name
    whisper_hailo = get_whisper_hailo()
    try:
        result = await whisper_service.transcribe_audio(whisper_hailo, audio_file_path=tmp_path)
    except Exception as e:
        system_logger.error(f"Error during transcription: {e}")
        response.status_code = 500
        return {"error": "An error occurred during transcription."}
    finally:
        whisper_hailo.stop()
        
    return {"message": result}


