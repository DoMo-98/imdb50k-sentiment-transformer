"""Utility functions for the Sentiment Analysis API."""

import numpy as np


def prediction_confidence(prob: float, thresh: float = 0.5) -> float:
    """
    Calculates the confidence of a binary prediction.

    Confidence measures how "far" the probability is from the decision threshold.
    Values close to the threshold have low confidence, extreme values (0.0, 1.0) have high confidence.
    """
    f1: float = prob / thresh
    f2: float = (1 - prob) / (1 - thresh)
    return 1 - 0.5 * np.minimum(f1, f2)
