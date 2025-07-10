FROM python:3.13-slim
ENV POETRY_VIRTUALENVS_REATE=false

WORKDIR app/
COPY . .


RUN pip install poetry

RUN poetry config installer.max-workers 10
RUN poetry install --no-interaction --no-ansi --without dev

EXPOSE 8000