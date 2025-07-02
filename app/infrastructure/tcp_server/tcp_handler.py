import logging
import json
import os

from tempfile import NamedTemporaryFile

from infrastructure.config.services_config import get_whisper_service
from infrastructure.config.whisper_hailo import get_whisper_hailo

system_logger = logging.getLogger(__name__)


async def handle_wyoming(reader, writer):

    response_data = None
    while True:
        data = await get_dict_from_tcp(reader)

        match data.get('type'):
            case "describe":
                response = await handle_describe_event()
                response_data = response.encode('utf-8')
                break

        writer.write(response_data)
        await writer.drain()


        # Read audio file from bytes
        # size_bytes = await reader.readexactly(4)
        # audio_size = int.from_bytes(size_bytes, 'big')
        # audio_data = await reader.readexactly(audio_size)

        # with NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        #     tmp.write(audio_data)
        #     tmp_path = tmp.name
        
        # # Main processing
        # whisper_hailo = get_whisper_hailo()
        
        # try:
        #     result = await whisper_service.transcribe_audio(whisper_hailo, audio_file_path=tmp_path)
        # except Exception as e:
        #     system_logger.error(f"Error during transcription: {e}")
        #     response.status_code = 500
        #     return {"error": "An error occurred during transcription."}
        # finally:
        #     whisper_hailo.stop()

        # system_logger.info("TCP: Speech to text result:", result)

        # # Prepare the response
        # text_bytes = result.encode("utf-8")
        # text_len = len(text_bytes)
        # writer.write(text_len.to_bytes(4, "big"))
        # writer.write(text_bytes)
        # await writer.drain()

    writer.close()
    await writer.wait_closed()


async def get_dict_from_tcp(reader):
    data = await reader.read(4096)
    if not data:
        return None
    system_logger.info(f"TCP: Received data before: {data}")
    result = json.loads(data.decode('utf-8'))
    system_logger.info(f"TCP: Received data after: {result}")

    return result

async def handle_describe_event():
    with open ("common/wyoming_describe_response.json", "r", encoding="utf-8") as file:
        # response = json.load(file) + "\n"
        result = file.read()
        system_logger.info(f"TCP: Sending describe response: {result}")
        return result
        # system_logger.info(f"response type: {type(response)}")
        # return response


# 192.168.178.45