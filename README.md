# Análisis de Sentimientos - Proyecto Deep Learning

Sistema de análisis de sentimientos para reseñas de cine usando mini-transformer (TensorFlow/Keras) con >70% de accuracy.

## Estructura del Proyecto

```
├── notebooks/proyecto_dl_eric_dominguez_morales.ipynb    # Entrenamiento y análisis
├── models/sentiment_analysis_serve_model/                # Modelo entrenado (SavedModel)
├── app/                                                  # API REST (FastAPI)
├── docs/data_scientist_diary.ipynb                       # Diario del científico
├── docker-compose.yml                                    # Docker setup
└── Dockerfile
```

## Uso Rápido

```bash
docker-compose up -d

curl -X POST "http://localhost:8000/api/v1/predict-sentiment" \
  -H "Content-Type: application/json" \
  -d '{"text": "This movie is amazing!"}'
```

## Componentes

- **`notebooks/`**: Código de entrenamiento, EDA y evaluación del modelo
- **`models/`**: Modelo final entrenado listo para producción
- **`app/`**: API REST completa (ver `app/README.md` para detalles)
- **`docs/`**: Diario del proceso de investigación (6 semanas de desarrollo)

---

**Proyecto Deep Learning - TokioSchool** | Eric Domínguez Morales