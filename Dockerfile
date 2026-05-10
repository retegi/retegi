FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gettext \
        gcc \
        libjpeg62-turbo-dev \
        zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . /app

RUN mkdir -p /app/data /app/media /app/staticfiles

EXPOSE 8000

# Gunicorn (el comando puede sobrescribirse en docker-compose)
CMD ["gunicorn", "retegi.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3", "--timeout", "120"]
