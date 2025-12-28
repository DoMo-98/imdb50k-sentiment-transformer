# Sentiment Analysis - Deep Learning Project

Sentiment analysis system for movie reviews using mini-transformer (TensorFlow/Keras) with >70% accuracy.

## Project Structure

```
├── notebooks/dl_project_eric_dominguez_morales.ipynb    # Training and analysis
├── models/sentiment_analysis_serve_model/                # Trained model (SavedModel)
├── app/                                                  # REST API (FastAPI)
├── docs/data_scientist_diary.ipynb                       # Data scientist diary
├── docker-compose.yml                                    # Docker setup
└── Dockerfile
```

## Quick Start

```bash
docker-compose up -d

curl -X POST "http://localhost:8000/api/v1/predict-sentiment" \
  -H "Content-Type: application/json" \
  -d '{"text": "This movie is amazing!"}'
```

## Components

- **`notebooks/`**: Training code, EDA and model evaluation
- **`models/`**: Final trained model ready for production
- **`app/`**: Complete REST API (see `app/README.md` for details)
- **`docs/`**: Research process diary (6 weeks of development)

---

**Deep Learning Project - TokioSchool** | Eric Dominguez Morales