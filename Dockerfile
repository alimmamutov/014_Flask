# dockerfile using poetry
FROM python:3.8.10-slim-buster

RUN apt-get update && apt-get install -y curl && apt-get install -y libpq-dev && apt-get install -y  build-essential

RUN curl -sSL https://install.python-poetry.org | POETRY_VERSION=1.0.5 POETRY_HOME=/root/poetry python -

ENV PATH="${PATH}:/root/poetry/bin"

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN poetry config virtualenvs.create false && poetry install --no-dev --no-root

COPY . /app/

EXPOSE 5000

CMD ["poetry", "run", "flask", "run", "--host=0.0.0.0", "--port=5000"]
