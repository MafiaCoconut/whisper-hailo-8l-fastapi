import os

class HefUtils:
    @staticmethod
    def get_encoder_hef_path(hw_arch):
        """
        Get the HEF path for the encoder based on the Hailo hardware architecture.

        Args:
            hw_arch (str): Hardware architecture ("hailo8" or "hailo8l").

        Returns:
            str: Path to the encoder HEF file.
        """
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
        if hw_arch == "hailo8l":
            hef_path = os.path.join(base_path, 'infrastructure', 'hefs', 'h8l', 'tiny', 'tiny-whisper-encoder-10s_15dB_h8l.hef')
        else:
            hef_path = os.path.join(base_path, 'hefs', 'h8', 'tiny', 'tiny-whisper-encoder-10s_15dB.hef')
        if not os.path.exists(hef_path):
            raise FileNotFoundError(f"Encoder HEF file not found: {hef_path}. Please check the path.")
        return hef_path

    @staticmethod
    def get_decoder_hef_path(hw_arch):
        """
        Get the HEF path for the decoder based on the Hailo hardware architecture and host type.

        Args:
            hw_arch (str): Hardware architecture ("hailo8" or "hailo8l").
            host (str): Host type ("x86" or "arm64").

        Returns:
            str: Path to the decoder HEF file.
        """
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
        if hw_arch == "hailo8l":
            hef_path = os.path.join(base_path, 'infrastructure', 'hefs', "h8l", "tiny",
                                    "tiny-whisper-decoder-fixed-sequence-matmul-split_h8l.hef")
        else:
            hef_path = os.path.join(base_path, "hefs", "h8", "tiny",
                                    "tiny-whisper-decoder-fixed-sequence-matmul-split.hef")
        if not os.path.exists(hef_path):
            raise FileNotFoundError(f"Decoder HEF file not found: {hef_path}. Please check the path.")
        return hef_path