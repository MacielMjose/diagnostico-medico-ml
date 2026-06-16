# WebAPI - API de Diagnóstico Médico

API REST para diagnóstico de SOP com FastAPI, integrando modelos de ML tabulares, classificação por imagem, otimização via Algoritmo Genético e explicação via LLM.

## Arquitetura

```
Cliente → /api/v1/*
              │
              ▼
         Routers (controllers)
              │
              ▼
         Services (lógica de negócio)
              │
         ┌────┴────┐
         ▼         ▼
  Infrastructure   Domain
  (LLM, models)    (entidades)
```

## Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| `GET` | `/health` | Health check |
| `POST` | `/api/v1/predict/` | Diagnóstico tabular (todas as features) |
| `POST` | `/api/v1/predict/top20` | Diagnóstico tabular (top-20 features) |
| `POST` | `/api/v1/ultrasound/predict` | Diagnóstico por imagem de ultrassom |
| `POST` | `/api/v1/optimize/` | Otimização de hiperparâmetros via Algoritmo Genético |
| `POST` | `/api/v1/explain/` | Explicação do diagnóstico via LLM |
| `GET` | `/docs` | Swagger UI (documentação interativa) |
| `GET` | `/redoc` | ReDoc (documentação alternativa) |

## Estrutura

```
WebAPI/
├── app/
│   ├── main.py                      # Factory + exception handlers
│   ├── core/                        # Config, logger, dependencies, exceptions
│   ├── domain/                      # Entidades, enums, exceções de domínio
│   ├── api/v1/                      # Routers (controllers) + schemas Pydantic
│   │   ├── predict/                 #    POST /predict e /predict/top20
│   │   ├── ultrasound/              #    POST /ultrasound/predict
│   │   ├── optimize/                #    POST /optimize
│   │   └── explain/                 #    POST /explain
│   ├── services/                    # Predictor, GeneticOptimizer, LLMExplainer
│   ├── infrastructure/              # ModelRegistry (cache LRU), LLMClient
│   └── monitoring/                  # TimingMiddleware, métricas Prometheus
├── models/                          # Modelos treinados (.pkl, .pth)
├── tests/                           # Testes unitários e de API
│   ├── unit/                        # Operadores genéticos
│   └── api/                         # Endpoints da API
├── docker/                          # Dockerfile + docker-compose
└── requirements.txt
```

## Setup

```bash
cd WebAPI

# Ambiente virtual (já existe .venv/)
python -m venv .venv
source .venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# (Opcional) Para endpoint de ultrassom:
pip install torch torchvision
```

## Exportar Modelos

Antes de rodar a API, exporte os modelos treinados dos notebooks:

```bash
# Adicione ao final do notebook Challenge_A/Tech_challenge_A_PCOS.ipynb:
import joblib
joblib.dump(pipeline, "WebAPI/models/logistic_regression.pkl")
joblib.dump(pipeline_top20, "WebAPI/models/logistic_regression_top20.pkl")

# Ou use o script auxiliar (requer dados):
python scripts/train_and_export.py
```

## Executar

```bash
# Desenvolvimento (com reload)
uvicorn app.main:app --reload --port 8000

# Produção
uvicorn app.main:app --host 0.0.0.0 --port 8000

# Docker
docker compose -f docker/docker-compose.yml up --build
```

## Testes

```bash
make test
# ou
pytest tests/ -v
```

## Algoritmo Genético

O endpoint `/api/v1/optimize/` recebe:

```json
{
  "population_size": 50,
  "mutation_rate": 0.05,
  "crossover_rate": 0.8,
  "generations": 20,
  "model_type": "xgboost"
}
```

O AG executa seleção por torneio, crossover de 1-ponto e mutação gaussiana, usando ROC AUC em 5-fold CV como função fitness. Retorna os melhores parâmetros, histórico de fitness e comparação com o modelo original.

## LLM Integration

O endpoint `/api/v1/explain/` envia um prompt para a LLM (OpenAI) com:

- **Role prompting**: "Você é um endocrinologista..."
- **Dados clínicos** do paciente
- **Diagnóstico** e **confiança** do modelo

Configure a chave da API no arquivo `.env`:

```env
LLM_API_KEY=sk-your-key
LLM_MODEL=gpt-4
```

## Monitoramento

- **Logging estruturado** com `structlog` (JSON)
- **Métricas Prometheus** via `prometheus-fastapi-instrumentator`
- **Middleware** de timing com header `X-Process-Time`
- **Health check** em `GET /health`

## Variáveis de Ambiente

| Variável | Default | Descrição |
|----------|---------|-----------|
| `MODEL_PATH` | `./models` | Caminho para os modelos treinados |
| `LLM_API_KEY` | — | Chave da API OpenAI |
| `LLM_MODEL` | `gpt-4` | Modelo LLM |
| `LOG_LEVEL` | `INFO` | Nível de log |
| `MAX_IMAGE_SIZE_MB` | `10` | Tamanho máximo de imagem (ultrassom) |

## Docker

```bash
cd WebAPI
docker compose -f docker/docker-compose.yml up --build
```

A API fica disponível em `http://localhost:8000/docs`.
