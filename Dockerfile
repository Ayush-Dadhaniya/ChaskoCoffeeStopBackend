# Use Python slim image as the base
FROM python:3.10-slim

# Set environment variables to prevent Python from writing bytecode and buffering stdout
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y gcc python3-dev musl-dev libpq-dev \
    && apt-get clean

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files into the container 
COPY . .

# Expose the application port
EXPOSE 8000

# Command to run the application
CMD ["uwsgi", "--http", "0.0.0.0:8000", "--module", "chasko_coffee_stop.wsgi:application"]
