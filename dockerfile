FROM python:3.10-slim
WORKDIR /carbon-aware-scheduler

RUN pip install poetry==1.6.1

COPY pyproject.toml poetry.lock ./
COPY carbon-aware-api-client .
RUN poetry install --no-root --no-dev
COPY ./src .


ENTRYPOINT [ "poetry", "run", "carbon-aware-scheduler" ]
