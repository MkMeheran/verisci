
FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml README.md ./
COPY src ./src
COPY tasks ./tasks
COPY tests ./tests

RUN pip install --no-cache-dir -e .

CMD ["pytest", "-v"]
