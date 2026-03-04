FROM cgr.dev/chainguard/python:3.14-dev AS builder

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_VIRTUALENVS_CREATE=true

WORKDIR /app

RUN pip install --no-cache-dir poetry==1.8.2

COPY pyproject.toml poetry.lock* ./

RUN poetry install --no-root --only main

FROM cgr.dev/chainguard/python:3.14

WORKDIR /app

COPY --from=builder /app/.venv /app/.venv
COPY . .

ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONUNBUFFERED=1

EXPOSE 80

ENTRYPOINT ["fastapi", "run", "src/main.py", "--port", "80"]