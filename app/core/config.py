from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    EMBEDDING_MODEL = os.getenv(
        "EMBEDDING_MODEL",
        "all-MiniLM-L6-v2"
    )


settings = Settings()