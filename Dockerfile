FROM python:3.12-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    pkg-config default-libmysqlclient-dev build-essential curl

# Install Node
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs

# Install pnpm
RUN npm install -g pnpm

# Set workdir
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Build frontend
WORKDIR /app/task_frontend
RUN pnpm install && pnpm run build

# Back to root
WORKDIR /app

# Collect static
RUN python manage.py collectstatic --noinput

CMD gunicorn personal_task_manager.wsgi:application --bind 0.0.0.0:8000
