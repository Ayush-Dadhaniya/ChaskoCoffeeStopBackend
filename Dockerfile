FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y gcc python3-dev musl-dev libpq-dev

# Install uwsgi
RUN pip install uwsgi

# Set the working directory in the container
WORKDIR /app

# Install required Python packages
COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Expose the application port
EXPOSE 8000

# Command to run the app using uWSGI
CMD ["uwsgi", "--http", ":8000", "--wsgi-file", "wsgi.py", "--master", "--processes", "4", "--threads", "2"]