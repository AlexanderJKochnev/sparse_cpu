import os


class Settings:
    model_dir: str = os.getenv(
        "MODEL_DIR",
        "/app/models/opensearch-neural-sparse-encoding-multilingual-v1",
    )
    cpu_threads: int = int(os.getenv("LABSE_CPU_THREADS", "4"))
    port: int = int(os.getenv("PORT", "8002"))


settings = Settings()