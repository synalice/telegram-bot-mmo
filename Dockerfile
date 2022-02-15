FROM python:3.9


COPY poetry.lock pyproject.toml alembic.ini telegram_bot_mmo/
WORKDIR telegram_bot_mmo/
RUN pip install poetry
RUN poetry install

COPY app telegram_bot_mmo/app

WORKDIR telegram_bot_mmo/
ENV PYTHONPATH=${PYTHONPATH}:${PWD}

ENTRYPOINT ["poetry", "run", "python"]
CMD ["app/main.py"]
