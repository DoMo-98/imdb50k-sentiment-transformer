# Sentiment Analysis API

REST API for real-time sentiment analysis using a custom Transformer model trained on the IMDB dataset.

## Features

- Binary sentiment classification (positive/negative)
- Confidence scores for predictions
- Preloaded model for fast inference
- Input validation and error handling
- Interactive API documentation

## Quick Start

**Important**: Docker files are in the project root, not in the `app/` folder.

### Docker (Recommended)
```bash
cd ..
docker-compose up -d
curl http://localhost:8000/health
```

## API Endpoints

### Health Check
```
GET /health
```

### Sentiment Prediction
```
POST /api/v1/predict-sentiment
Content-Type: application/json

{
  "text": "This movie is amazing!"
}
```

Response:
```json
{
  "sentiment": "positive",
  "confidence": 0.9988,
  "text": "This movie is amazing!"
}
```

### Model Information
```
GET /api/v1/model-info
```

## Input Validation

- Text length: 1-5000 characters
- Text cannot be empty or contain only spaces
- Returns appropriate HTTP status codes (200, 400, 422, 500)

## Configuration

The default configuration is defined in `core/config.py`. No additional configuration is required.

## Documentation

Once running, access:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Model Information

- Type: Custom mini-transformer
- Dataset: IMDB 50k movie reviews
- Accuracy: >70%
- Format: TensorFlow SavedModel
- Preprocessing: Built into the model

---

**Deep Learning Project - TokioSchool** | Eric Dominguez Morales