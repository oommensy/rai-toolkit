# RAI Toolkit Docker Image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Install pre-commit hooks
RUN pre-commit install --install-hooks

# Create non-root user for security
RUN useradd -m -u 1000 rai-user && chown -R rai-user:rai-user /app
USER rai-user

# Set environment variables
ENV PYTHONPATH=/app
ENV RAI_CONFIG_PATH=/app/config

# Default command
CMD ["python", "-c", "print('RAI Toolkit ready! Use: python tools/<tool_name>.py --help')"]

# Labels for metadata
LABEL maintainer="RAI Toolkit Team"
LABEL description="Responsible AI Toolkit - Build, evaluate, and govern AI systems responsibly"
LABEL version="1.0.0"