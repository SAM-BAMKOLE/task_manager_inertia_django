#!/bin/bash
set -eux

# Install system dependencies for mysqlclient
apt-get update
apt-get install -y pkg-config default-libmysqlclient-dev build-essential

# Install Node.js and pnpm
apt-get install -y nodejs
npm install -g pnpm

# Install Python dependencies
pip install --no-cache-dir -r requirements.txt

# Install Node dependencies and build Vite assets with pnpm
cd task_frontend
pnpm install
pnpm run build

# Collect Django static files
cd ..
python manage.py collectstatic --noinput