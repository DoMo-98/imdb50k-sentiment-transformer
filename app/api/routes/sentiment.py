import logging
from typing import Any, Dict

from fastapi import APIRouter, HTTPException, status

from app.schemas.sentiment import ErrorResponse, SentimentRequest, SentimentResponse
from app.services.sentiment_service import sentiment_service

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post(
    "/predict-sentiment",
    response_model=SentimentResponse,
    responses={
        400: {"model": ErrorResponse, "description": "Bad Request"},
        422: {"model": ErrorResponse, "description": "Validation Error"},
        500: {"model": ErrorResponse, "description": "Internal Server Error"},
    },
    summary="Predict sentiment of text",
    description=(
        "Analyze the sentiment of the provided text and return a prediction "
        "with confidence score. The model classifies text as either 'positive' "
        "or 'negative' sentiment."
    ),
)
async def predict_sentiment(request: SentimentRequest) -> SentimentResponse:
    """
    Predict the sentiment of the provided text.

    - **text**: The text to analyze (required, 1-5000 characters)

    Returns:
    - **sentiment**: Either "positive" or "negative"
    - **confidence**: Confidence score between 0.0 and 1.0
    - **text**: The original text that was analyzed
    """
    try:
        logger.info(
            f"Processing sentiment analysis request for text length: {len(request.text)}"
        )

        sentiment, confidence = await sentiment_service.predict_sentiment_async(
            request.text
        )

        response = SentimentResponse(
            sentiment=sentiment, confidence=round(confidence, 4), text=request.text
        )

        logger.info(f"Successfully processed request: {sentiment} ({confidence:.4f})")

        return response

    except ValueError as e:
        logger.warning(f"Validation error: {str(e)}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    except RuntimeError as e:
        logger.error(f"Model error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to process sentiment analysis request",
        )

    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred",
        )


@router.get(
    "/model-info",
    summary="Get model information",
    description="Get information about the sentiment analysis model",
)
async def get_model_info() -> Dict[str, Any]:
    """Get information about the loaded model."""
    try:
        return {
            "model_loaded": sentiment_service.model_loaded,
            "model_endpoint": "serve",
            "confidence_threshold": 0.5,
            "supported_sentiments": ["positive", "negative"],
            "max_text_length": 5000,
        }
    except Exception as e:
        logger.error(f"Error getting model info: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to get model information",
        )
