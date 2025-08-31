# Use slim version for smaller image size
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=myproject.settings

# Install system dependencies including curl
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        curl \
        gcc \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && pip install gunicorn

# Copy project files
COPY . .

# Create static files directory and collect static
RUN mkdir -p staticfiles \
    && python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "--timeout", "120", "myproject.wsgi:application"]
