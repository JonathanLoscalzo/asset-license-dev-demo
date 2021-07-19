# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.9-slim-buster

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install and setup poetry
# RUN pip install -U pip \
#     && apt-get update \
#     && apt install -y curl netcat \
#     && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
# ENV PATH="${PATH}:/root/.poetry/bin"

RUN pip install poetry

# Install pip requirements
# COPY requirements.txt .
# RUN python -m pip install -r requirements.txt

WORKDIR /app

RUN poetry config virtualenvs.create false

COPY poetry.lock pyproject.toml ./
RUN poetry install --no-dev

COPY . .
RUN poetry install --no-dev

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

RUN pip install uvicorn

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["uvicorn", "src.asset_manager.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
# CMD [ "python", "src/asset_manager/main.py" ]

# FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

# COPY . /app/app