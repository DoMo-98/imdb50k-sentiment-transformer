# API de Análisis de Sentimientos

API REST para análisis de sentimientos en tiempo real usando un modelo Transformer personalizado entrenado en el dataset IMDB.

## Características

- Clasificación binaria de sentimientos (positivo/negativo)
- Puntuaciones de confianza para las predicciones
- Modelo precargado para inferencia rápida
- Validación de entrada y manejo de errores
- Documentación interactiva de la API

## Inicio Rápido

**Importante**: Los archivos Docker están en la raíz del proyecto, no en la carpeta `app/`.

### Docker (Recomendado)
```bash
cd ..
docker-compose up -d
curl http://localhost:8000/health
```

## Endpoints de la API

### Verificación de Estado
```
GET /health
```

### Predicción de Sentimiento
```
POST /api/v1/predict-sentiment
Content-Type: application/json

{
  "text": "This movie is amazing!"
}
```

Respuesta:
```json
{
  "sentiment": "positive",
  "confidence": 0.9988,
  "text": "This movie is amazing!"
}
```

### Información del Modelo
```
GET /api/v1/model-info
```

## Validación de Entrada

- Longitud del texto: 1-5000 caracteres
- El texto no puede estar vacío o contener solo espacios
- Retorna códigos de estado HTTP apropiados (200, 400, 422, 500)

## Configuración

La configuración por defecto está definida en `core/config.py`. No se requiere configuración adicional.

## Documentación

Una vez ejecutándose, accede a:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Información del Modelo

- Tipo: Mini-transformer personalizado
- Dataset: IMDB 50k reseñas de películas
- Precisión: >70%
- Formato: TensorFlow SavedModel
- Preprocesamiento: Integrado en el modelo

---

**Proyecto Deep Learning - TokioSchool** | Eric Domínguez Morales