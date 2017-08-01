# Use an official Python runtime as a parent image
FROM python:2.7-slim

RUN pip install kubernetes \
                flask

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD job-trigger.py /app
ADD job-template.yaml /app

EXPOSE 8080

# Run app.py when the container launches
CMD ["python", "job-trigger.py"]
