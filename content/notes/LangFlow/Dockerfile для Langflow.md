Треба створити Dockerfile для запуску застосунку [Langflow](https://github.com/logspace-ai/langflow) на архітектурі arm64v8arm64v8. За основу можна взяти наступний код:  

``` Dockerfile
FROM python:3.10-slim

WORKDIR /app

# Install Poetry
RUN apt-get update && apt-get install gcc g++ curl build-essential postgresql-server-dev-all -y
RUN curl -sSL https://install.python-poetry.org | python3 -
# # Add Poetry to PATH
ENV PATH="${PATH}:/root/.local/bin"
# # Copy the pyproject.toml and poetry.lock files
COPY poetry.lock pyproject.toml ./
# Copy the rest of the application codes
COPY ./ ./

# Install dependencies
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

CMD ["uvicorn", "langflow.main:app", "--host", "0.0.0.0", "--port", "5003", "--reload", "log-level", "debug"]
```

``` Dockerfile
# Use arm64v8 compatible Python image
FROM arm64v8/python:3.10-slim

WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install gcc g++ curl build-essential postgresql-server-dev-all -y

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Add Poetry to PATH
ENV PATH="${PATH}:/root/.local/bin"

# Copy the pyproject.toml and poetry.lock files
COPY poetry.lock pyproject.toml ./

# Copy the rest of the application codes
COPY ./ ./

# Install dependencies using Poetry
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

# Start the application
CMD ["uvicorn", "langflow.main:app", "--host", "0.0.0.0", "--port", "5003", "--reload", "log-level", "debug"]
```