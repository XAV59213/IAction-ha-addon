ARG BUILD_FROM=docker.io/library/python:3.12
FROM ${BUILD_FROM}

LABEL org.opencontainers.image.source="https://github.com/lfpoulain/iaction-ha-addon" \
      org.opencontainers.image.title="IAction (Home Assistant add-on)" \
      org.opencontainers.image.description="Image analysis with AI + MQTT, web UI, and Home Assistant integration" \
      org.opencontainers.image.licenses="MIT"

# Install dependencies
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    python3-opencv \
    ffmpeg \
  && rm -rf /var/lib/apt/lists/*

# Create app directory & fetch source code
WORKDIR /app
RUN git clone --depth 1 https://github.com/lfpoulain/IAction.git .

# Create and populate virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Ensure /tmp is writable for FFmpeg
RUN mkdir -p /tmp && chmod 777 /tmp

# Copy entrypoint script
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Start application
ENTRYPOINT ["/app/entrypoint.sh"]
