FROM python:3.12-slim

# Install packages for mysqlclient 
RUN apt-get update && apt-get install -y \
    git \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    default-mysql-client \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
