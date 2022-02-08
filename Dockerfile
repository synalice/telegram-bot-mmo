FROM python:3.8


COPY app telegram_bot_mmo/app
COPY poetry.lock pyproject.toml alembic.ini telegram_bot_mmo/

WORKDIR telegram_bot_mmo/
ENV PYTHONPATH=${PYTHONPATH}:${PWD}

RUN pip install poetry
RUN poetry install

CMD poetry run python app/main.py
