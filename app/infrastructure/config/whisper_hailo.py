import logging
from fastapi import FastAPI
from application.pipelines.hailo_whisper_pipeline import HailoWhisperPipeline
from infrastructure.config.utils_config import hef_utils, args_utils

# whisper_hailo = None
# encoder_path = hef_utils.get_encoder_hef_path(variant)
# decoder_path = hef_utils.get_decoder_hef_path(variant)

# print(f"encoder_path: {encoder_path}")
# print(f"decoder_path: {decoder_path}")
system_logger = logging.getLogger(__file__)
# whisper_hailo: HailoWhisperPipeline | None = None
# whisper_hailo = HailoWhisperPipeline(
#     encoder_model_path=encoder_path,
#     decoder_model_path=decoder_path,
#     variant='tiny',
#     multi_process_service=False)

hailo_model = ""
encoder_path = ""
decoder_path = ""


def config(app: FastAPI, _model: str = "hailo8l") -> None:
    system_logger.info(f"Configuring Whisper Hailo with model: {_model}")
    global hailo_model
    hailo_model = _model

    global encoder_path
    encoder_path = hef_utils.get_encoder_hef_path(_model)

    global decoder_path
    decoder_path = hef_utils.get_decoder_hef_path(_model)


    # encoder_path = hef_utils.get_encoder_hef_path(model)
    # decoder_path = hef_utils.get_decoder_hef_path(model)

    # app.state.whisper_hailo = HailoWhisperPipeline(
    #     encoder_model_path=encoder_path,
    #     decoder_model_path=decoder_path,
    #     variant='tiny',
    #     multi_process_service=False)
    system_logger.info(f"Configuring Whisper Hailo was successful")


def whisper_hailo_stop():
    whisper_hailo.stop()

def get_whisper_hailo() -> HailoWhisperPipeline:
    whisper_hailo = HailoWhisperPipeline(
        encoder_model_path=encoder_path,
        decoder_model_path=decoder_path,
        variant='tiny',
        multi_process_service=False)

    return whisper_hailo