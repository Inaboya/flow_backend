FROM python:3.13-slim
WORKDIR /app

# Install system dependencies for postgres
RUN apt-get update && apt-get install -y libpq-dev gcc

COPY apps/python-engine/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY apps/python-engine/ .

EXPOSE 8000
CMD ["python", "-m", "src.main"]