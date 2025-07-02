from wyoming.info import AsrModel, AsrProgram, Attribution, Info

wyoming_info = Info(
    asr=[
        AsrProgram(
            name="whisper-hailo-8l-fastapi",
            description="Whisper with Hailo-8(L) support on FastAPI Server",
            attribution=Attribution(
                name="MafiaCoconut",
                url="https://github.com/MafiaCoconut/whisper-hailo-8l-fastapi/",
            ),
            installed=True,
            version="0.0.1",
            models=[
                AsrModel(
                    name="whisper-hailo",
                    description="whisper-hailo",
                    attribution=Attribution(
                        name="HAILO",
                        url="https://hailo.ai/products/ai-accelerators/hailo-8-ai-accelerator/",
                    ),
                    installed=True,
                    languages=["en"],
                    version="4.2.1",
                )
            ],
        )
    ],
)