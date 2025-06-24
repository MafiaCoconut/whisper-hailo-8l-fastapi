from application.pipelines.hailo_whisper_pipeline import HailoWhisperPipeline
from infrastructure.config.utils_config import hef_utils, args_utils

# whisper_hailo = None
variant = "hailo8l"
# encoder_path = hef_utils.get_encoder_hef_path(variant)
# decoder_path = hef_utils.get_decoder_hef_path(variant)

# print(f"encoder_path: {encoder_path}")
# print(f"decoder_path: {decoder_path}")

whisper_hailo: HailoWhisperPipeline | None = None
# whisper_hailo = HailoWhisperPipeline(
#     encoder_model_path=encoder_path,
#     decoder_model_path=decoder_path,
#     variant='tiny',
#     multi_process_service=False)

def config():
    # args = args_utils.get_args()
    variant = "hailo8l"
    encoder_path = hef_utils.get_encoder_hef_path(variant)
    decoder_path = hef_utils.get_decoder_hef_path(variant)


    global whisper_hailo
    whisper_hailo = HailoWhisperPipeline(
        encoder_model_path=encoder_path,
        decoder_model_path=decoder_path,
        variant='tiny',
        multi_process_service=False)

def whisper_hailo_stop():
    whisper_hailo.stop()