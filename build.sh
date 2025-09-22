#!/bin/bash
set -eux

# Install system dependencies for mysqlclient
apt-get update
apt-get install -y pkg-config default-libmysqlclient-dev build-essential curl

# Install Node.js and npm
apt-get install -y nodejs npm || {
    # Fallback: Install Node.js and npm via nodesource if apt fails
    curl -fsSL https://deb.nodesource.com/setup_20.x | bash -
    apt-get install -y nodejs
}

# Install pnpm globally
npm install -g pnpm || {
    # Fallback: Install pnpm directly if npm fails
    curl -fsSL https://get.pnpm.io/install.sh | sh -
    export PNPM_HOME="/root/.local/share/pnpm"
    export PATH="$PNPM_HOME:$PATH"
}

# Install Python dependencies
pip install --no-cache-dir -r requirements.txt

# Install Node dependencies and build Vite assets with pnpm
cd task_frontend
pnpm install
pnpm run build

# Collect Django static files
cd ..
python manage.py collectstatic --noinput