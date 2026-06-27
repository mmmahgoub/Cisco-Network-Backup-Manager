# Use an official, lightweight Python runtime
FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir flask netmiko


COPY . .


EXPOSE 5000

CMD ["python", "app.py"]