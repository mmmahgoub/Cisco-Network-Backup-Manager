# Use an official, lightweight Python runtime
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Install system dependencies that might be needed for Netmiko/Paramiko (cryptography)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies directly
RUN pip install --no-cache-dir flask netmiko

# Copy the application code into the container
COPY . .

# Expose Flask's default port
EXPOSE 5000

# Run the application (binding to 0.0.0.0 so it's accessible outside the container)
CMD ["python", "app.py"]