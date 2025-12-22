import os
from typing import List

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""

    PROJECT_NAME: str = "Sentiment Analysis API"
    PROJECT_DESCRIPTION: str = (
        "A REST API for sentiment analysis using a pre-trained Transformer model. "
        "Classifies text as positive or negative sentiment with confidence scores."
    )
    VERSION: str = "1.0.0"

    ALLOWED_HOSTS: List[str] = ["*"]

    MODEL_PATH: str = "models/sentiment_analysis_serve_model"
    MODEL_ENDPOINT: str = "serve"
    CONFIDENCE_THRESHOLD: float = 0.5

    LOG_LEVEL: str = "INFO"

    class Config:
        case_sensitive = True


settings = Settings()
