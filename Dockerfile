# Pull base image
FROM python:3.7

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copy project
COPY . /code/

# Copy production settings
COPY .env.prod /code/.env

RUN chmod +x docker-entrypoint.sh

ENTRYPOINT ["/code/docker-entrypoint.sh"]
