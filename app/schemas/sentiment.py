from typing import Literal

from pydantic import BaseModel, Field, validator


class SentimentRequest(BaseModel):
    """Request schema for sentiment analysis."""

    text: str = Field(
        ...,
        description="Text to analyze for sentiment",
        example="This movie was absolutely fantastic! Great acting and plot.",
        min_length=1,
        max_length=5000,
    )

    @validator("text")
    def validate_text(cls, v):
        """Validate text input."""
        if not v or not v.strip():
            raise ValueError("Text cannot be empty or only whitespace")
        return v.strip()

    class Config:
        json_schema_extra = {
            "example": {
                "text": "This movie was absolutely fantastic! Great acting and plot."
            }
        }


class SentimentResponse(BaseModel):
    """Response schema for sentiment analysis."""

    sentiment: Literal["positive", "negative"] = Field(
        ..., description="Predicted sentiment of the text"
    )

    confidence: float = Field(
        ...,
        description="Confidence score of the prediction (0.0 to 1.0)",
        ge=0.0,
        le=1.0,
    )

    text: str = Field(..., description="Original text that was analyzed")

    class Config:
        json_schema_extra = {
            "example": {
                "sentiment": "positive",
                "confidence": 0.95,
                "text": "This movie was absolutely fantastic! Great acting and plot.",
            }
        }


class ErrorResponse(BaseModel):
    """Error response schema."""

    error: str = Field(..., description="Error message")

    detail: str = Field(None, description="Detailed error information")

    class Config:
        json_schema_extra = {
            "example": {"error": "Validation Error", "detail": "Text cannot be empty"}
        }
