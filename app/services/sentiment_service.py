import logging
from pathlib import Path
from typing import Tuple

import numpy as np
import tensorflow as tf
import tensorflow_text

from app.core.config import settings
from app.utils import prediction_confidence

logger = logging.getLogger(__name__)


class SentimentAnalysisService:
    """Service for sentiment analysis using TensorFlow SavedModel."""

    def __init__(self):
        self.model = None
        self.model_loaded = False

    def load_model(self) -> None:
        """Load the TensorFlow SavedModel."""
        try:
            current_dir = Path(__file__).parent.parent.parent
            model_path = current_dir / settings.MODEL_PATH

            if not model_path.exists():
                raise FileNotFoundError(f"Model not found at {model_path}")

            logger.info(f"Loading model from: {model_path}")

            self.model = tf.keras.layers.TFSMLayer(
                str(model_path), call_endpoint=settings.MODEL_ENDPOINT
            )

            test_input = tf.constant(["This is a test"])
            _ = self.model(test_input)

            self.model_loaded = True
            logger.info("Model loaded successfully")

        except Exception as e:
            logger.error(f"Failed to load model: {str(e)}")
            raise RuntimeError(f"Failed to load sentiment analysis model: {str(e)}")

    def predict_sentiment(self, text: str) -> Tuple[str, float]:
        """
        Predict sentiment for a given text.

        Args:
            text: Input text to analyze

        Returns:
            Tuple of (sentiment, confidence) where sentiment is 'positive' or 'negative'
            and confidence is the probability score
        """
        if not self.model_loaded:
            raise RuntimeError("Model not loaded. Call load_model() first.")

        try:
            inputs = tf.constant([text])

            prediction = self.model(inputs)

            probability = float(prediction.numpy()[0][0])

            sentiment = (
                "positive"
                if probability >= settings.CONFIDENCE_THRESHOLD
                else "negative"
            )
            confidence = prediction_confidence(
                probability, settings.CONFIDENCE_THRESHOLD
            )

            logger.info(
                f"Predicted sentiment: {sentiment} (confidence: {confidence:.4f})"
            )

            return sentiment, confidence

        except Exception as e:
            logger.error(f"Prediction failed: {str(e)}")
            raise RuntimeError(f"Failed to analyze sentiment: {str(e)}")

    async def predict_sentiment_async(self, text: str) -> Tuple[str, float]:
        """
        Async wrapper for sentiment prediction.

        Args:
            text: Input text to analyze

        Returns:
            Tuple of (sentiment, confidence)
        """
        return self.predict_sentiment(text)


sentiment_service = SentimentAnalysisService()
