FROM python:3.12-slim
LABEL authors="Maxim Dvoretsky <mx.dvoretsky@gmail.com>"

ENV PYTHONUNBUFFERED=1

EXPOSE 8000
WORKDIR /app

RUN apt-get update && apt-get install -y curl \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV PATH="/root/.local/bin:$PATH"

COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.create false
RUN poetry install --no-root

COPY . .

CMD poetry run uvicorn --host=0.0.0.0 --port=8000 app.main:app