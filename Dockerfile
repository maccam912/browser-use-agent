FROM python:3.13-slim

WORKDIR /app

# Install UV and Xvfb dependencies
RUN apt-get update \
    && apt-get install -y curl xvfb x11-utils \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && curl -LsSf https://astral.sh/uv/install.sh | sh

# Copy project files
COPY pyproject.toml ./

# Install Playwright browsers
RUN /root/.local/bin/uv run playwright install --with-deps \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY main.py ./

# Set up a virtual display
ENV DISPLAY=:99

# Create an entrypoint script to start Xvfb before the main program
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Use ENTRYPOINT with the script that starts Xvfb
ENTRYPOINT ["/entrypoint.sh"]