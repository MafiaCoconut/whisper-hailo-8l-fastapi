import argparse

class ArgsUtils:
    @staticmethod
    def get_args():
        """
        Initialize and run the argument parser.

        Return:
            argparse.Namespace: Parsed arguments.
        """
        parser = argparse.ArgumentParser(description="Whisper Hailo Pipeline")
        parser.add_argument(
            "--reuse-audio",
            action="store_true",
            help="Reuse the previous audio file (sampled_audio.wav)"
        )
        parser.add_argument(
            "--hw-arch",
            type=str,
            default="hailo8l",
            choices=["hailo8", "hailo8l"],
            help="Hardware architecture to use (default: hailo8)"
        )
        parser.add_argument(
            "--multi-process-service",
            action="store_true",
            help="Enable multi-process service to run other models in addition to Whisper"
        )
        return parser.parse_args()