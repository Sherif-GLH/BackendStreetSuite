# Use the official Python image from the Docker Hub
FROM python:3.12.4-slim-bullseye
# Set environment variables to prevent Python from writing pyc files and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
# Update the package list and install system dependencies
RUN apt-get update && apt-get -y install \
    gcc \
    libpq-dev \
    default-libmysqlclient-dev \
    pkg-config \
    wget \
    curl \
    unzip && \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt-get install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb && \
    apt-get clean
# Install Chromedriver
RUN CHROMEDRIVER_VERSION=$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE) && \
    wget -N https://chromedriver.storage.googleapis.com/100.0.4896.60/chromedriver_linux64.zip -P /tmp && \
    unzip /tmp/chromedriver_linux64.zip -d /tmp && \
    mv /tmp/chromedriver /usr/local/bin/chromedriver && \
    chmod +x /usr/local/bin/chromedriver && \
    rm /tmp/chromedriver_linux64.zip
# Set the working directory in the container
WORKDIR /app
# Copy the requirements file to the working directory
COPY requirements.txt /app/requirements.txt
# Install the dependencies
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt
# Copy the current directory contents into the container at /app
COPY . /app/
# Expose port 8000 to the outside world
EXPOSE 8000
# Command to run the Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]