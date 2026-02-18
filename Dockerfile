# Stage 1: Build
FROM python:3.10-slim as builder

# Set working directory to /app
WORKDIR /app

# Copy poetry files
COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction

# Copy application code
COPY . .

# Build wheels for dependencies
RUN pip wheel . -w /app/wheels

# Stage 2: Runtime
FROM python:3.10-slim

# Set working directory to /app
WORKDIR /app

# Create non-root user
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Set ownership of /app to appuser
RUN chown -R appuser:appuser /app

# Copy wheels from Stage 1
COPY --from=builder --chown=appuser:appuser /app/wheels /app/wheels

# Install dependencies
RUN --mount=type=bind,src=/app/wheels,target=/app/wheels \
    pip install --no-cache-dir --no-index --find-links=/app/wheels .

# Copy application code
COPY --chown=appuser:appuser . .

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set command to run Celery worker
CMD ["celery", "-A", "AutoDocGen", "worker", "--loglevel=info"]

# Set user to appuser
USER appuser

# Health check
HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
    CMD ["python", "-c", "import redis; redis.Redis(host='redis', port=6379, db=0).ping()"]

# Expose port for Redis
EXPOSE 6379
