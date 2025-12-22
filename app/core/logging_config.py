import logging
import sys
from typing import Optional

from app.core.config import settings


def setup_logging(log_level: Optional[str] = None) -> None:
    """Setup logging configuration."""

    level = log_level or settings.LOG_LEVEL

    logging.basicConfig(
        level=getattr(logging, level.upper()),
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[logging.StreamHandler(sys.stdout)],
    )

    logging.getLogger("uvicorn").setLevel(logging.INFO)
    logging.getLogger("uvicorn.access").setLevel(logging.INFO)
    logging.getLogger("tensorflow").setLevel(logging.ERROR)

    import os

    os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
