# Use a base image with Python and Node.js
FROM python:3.12-slim

# Install Node.js, npm, and MySQL dependencies
RUN apt-get update && apt-get install -y \
    nodejs \
    npm \
    pkg-config \
    default-libmysqlclient-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy frontend package.json and install Node dependencies (for Vite)
COPY task_frontend/package.json task_frontend/package-lock.json ./task_frontend/
RUN cd task_frontend && npm ci

# Copy Python requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Build Vite assets (assumes vite.config.js outputs to static/dist)
RUN cd task_frontend && npm run build

# Collect Django static files
RUN python manage.py collectstatic --noinput

# Expose the port (Leapcell assigns dynamically via $PORT)
EXPOSE $PORT

# Run migrations and start Gunicorn
CMD ["sh", "-c", "python manage.py migrate && gunicorn personal_task_manager.wsgi:application --bind 0.0.0.0:$PORT"]