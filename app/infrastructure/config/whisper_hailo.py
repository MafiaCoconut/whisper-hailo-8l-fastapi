from application.pipelines.hailo_whisper_pipeline import HailoWhisperPipeline
from infrastructure.config.utils_config import hef_utils, args_utils

whisper_hailo = None
def config():
    args = args_utils.get_args()

    encoder_path = hef_utils.get_encoder_hef_path(args.hw_arch)
    decoder_path = hef_utils.get_decoder_hef_path(args.hw_arch)


    global whisper_hailo
    whisper_hailo = HailoWhisperPipeline(
        encoder_model_path=encoder_path,
        decoder_model_path=decoder_path,
        variant='tiny',
        multi_process_service=args.multi_process_service)

def whisper_hailo_stop():
    whisper_hailo.stop()