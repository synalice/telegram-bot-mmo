FROM python:3.9


COPY poetry.lock pyproject.toml alembic.ini telegram-bot-mmo/
WORKDIR telegram-bot-mmo/
RUN pip install poetry
RUN poetry install --no-root

COPY app app

ENV PYTHONPATH=${PYTHONPATH}:${PWD}

ENTRYPOINT ["poetry", "run", "python"]
CMD ["app/main.py"]

# This line is for debugging purposes. Uncomment if you need the container to run forever so that you can exec into it.
# ONLY use this for debugging purposes.
#ENTRYPOINT ["tail", "-f", "/dev/null"]
