import logging

import tensorflow as tf
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import sentiment
from app.core.config import settings
from app.core.logging_config import setup_logging
from app.services.sentiment_service import sentiment_service

setup_logging()
logger = logging.getLogger(__name__)

tf.get_logger().setLevel("ERROR")


def create_application() -> FastAPI:
    """Create and configure the FastAPI application."""

    app = FastAPI(
        title=settings.PROJECT_NAME,
        description=settings.PROJECT_DESCRIPTION,
        version=settings.VERSION,
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_HOSTS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(sentiment.router, prefix="/api/v1", tags=["sentiment"])

    @app.on_event("startup")
    async def startup_event():
        """Initialize services on startup."""
        logger.info("Starting Sentiment Analysis API...")
        logger.info(f"TensorFlow version: {tf.__version__}")

        try:
            logger.info("Loading sentiment analysis model...")
            sentiment_service.load_model()
            logger.info("Model loaded successfully!")
        except Exception as e:
            logger.error(f"Failed to load model on startup: {str(e)}")
            raise RuntimeError(f"Cannot start API without model: {str(e)}")

    @app.on_event("shutdown")
    async def shutdown_event():
        """Cleanup on shutdown."""
        logger.info("Shutting down Sentiment Analysis API...")

    @app.get("/", tags=["health"])
    async def root():
        """Health check endpoint."""
        return {
            "message": "Sentiment Analysis API is running",
            "version": settings.VERSION,
            "status": "healthy",
        }

    @app.get("/health", tags=["health"])
    async def health_check():
        """Detailed health check endpoint."""
        return {
            "status": "healthy",
            "version": settings.VERSION,
            "tensorflow_version": tf.__version__,
        }

    return app


app = create_application()
