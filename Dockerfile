FROM python:3.10

# Install dependencies
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copy project files into container
COPY . /code/

# Expose port for the container
EXPOSE 8000

# Set the entry point to uWSGI
CMD ["uwsgi", "--http", "0.0.0.0:8000", "--module", "chasko_coffee_stop.wsgi:application", "--master", "--processes", "4", "--threads", "2"]