FROM python:3.8


COPY app /app
COPY poetry.lock pyproject.toml /app/
WORKDIR app

RUN pip install poetry
RUN poetry install
ENV PYTHONPATH "${PYTHONPATH}:/usr/bin/python3.8"
ENV PYTHONPATH "${PYTHONPATH}:/"

CMD poetry run python main.py
