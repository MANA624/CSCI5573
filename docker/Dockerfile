# Use an official Python runtime as a parent image
FROM python:3.4-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Random liines of code from the internet
FROM alpine:3.5
RUN apk add --no-cache python3 && python3 -m ensurepip && rm -r /usr/lib/python*/ensurepip && pip3 install --upgrade pip setuptools && rm -r /root/.cache
RUN apk add --update build-base vim curl bash zip git linux-headers python3-dev py-psutil && rm -rf /var/cache/apk/*

# Install any needed packages specified in requirements.txt
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]

