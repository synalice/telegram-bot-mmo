FROM python:3.9


COPY app telegram_bot_mmo/app
COPY poetry.lock pyproject.toml alembic.ini telegram_bot_mmo/

WORKDIR telegram_bot_mmo/
ENV PYTHONPATH=${PYTHONPATH}:${PWD}

RUN pip install poetry
RUN poetry install

ENTRYPOINT ["poetry", "run", "python"]
CMD ["app/main.py"]
