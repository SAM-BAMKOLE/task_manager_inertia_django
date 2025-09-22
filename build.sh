#!/bin/bash
set -eux

# Install system dependencies for mysqlclient
apt-get update
apt-get install -y pkg-config default-libmysqlclient-dev build-essential

# Install Node.js and npm (for Vite)
apt-get install -y nodejs npm

# Install Python dependencies
pip install --no-cache-dir -r requirements.txt

# Install Node dependencies and build Vite assets
cd task_frontend
npm ci
npm run build

# Collect Django static files
cd ..
python manage.py collectstatic --noinput