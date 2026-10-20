
FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY pipeline.py config.yaml ./
COPY module4_pipeline ./module4_pipeline

ENTRYPOINT ["python", "pipeline.py"]
