FROM --platform=linux/amd64 python:3.10-slim

# Set environment variables
ENV PATH="/usr/local/bin:$PATH"
ENV PYTHONUNBUFFERED=1
ENV SELENIUM_HUB_HOST="selenium-hub"
ENV SELENIUM_HUB_PORT="4444"
ENV EXTENSION_PATH="/opt/extension"

# Create working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy test files
COPY . /app


