# WebAPI - API de Diagnóstico Médico

API REST desenvolvida com FastAPI para servir o modelo de predição de diagnóstico médico (SOP).

## Stack

- **Python** 3.12+
- **FastAPI** 0.137
- **Uvicorn** 0.49
- **Pydantic** 2.13

## Pré-requisitos

- Python 3.12 ou superior
- [pyenv](https://github.com/pyenv/pyenv) (recomendado) ou virtualenv

## Instalação

```bash
cd WebAPI

# Criar e ativar ambiente virtual (opcional, já existe .venv/)
python -m venv .venv
source .venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
```

## Execução

```bash
uvicorn app.main:app --reload
```

Acessar em: [http://localhost:8000](http://localhost:8000)

Documentação interativa (Swagger): [http://localhost:8000/docs](http://localhost:8000/docs)

## Endpoints

| Método | Rota   | Descrição         |
|--------|--------|-------------------|
| GET    | `/`    | Hello World       |

## Estrutura

```
WebAPI/
├── app/
│   └── main.py          # Aplicação FastAPI e rotas
├── .venv/               # Ambiente virtual Python
├── requirements.txt     # Dependências do projeto
└── README.md            # Este arquivo
```

## Próximos passos

- Integração com modelo ML treinado
- Endpoints de predição
- Schemas Pydantic para validação
- Testes automatizados
- Dockerização
