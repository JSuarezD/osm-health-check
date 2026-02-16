
FROM python:3.14

ENV POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=false \
    PATH="/opt/poetry/bin:$PATH"


RUN curl -sSL https://install.python-poetry.org | python3 -
    
    
WORKDIR /code


COPY pyproject.toml poetry.lock* ./


RUN poetry install --no-interaction --no-ansi --no-root



COPY . . 


CMD ["fastapi", "run", "src/main.py", "--port", "80"]