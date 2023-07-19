# Use the official Python image as the base image
FROM python:3.9-slim

# Set working directory in the container
WORKDIR /app

# Copy the Python files and requirements.txt
COPY app.py bsc_functions.py requirements.txt ./

# Install required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port on which the Flask app runs
EXPOSE 8000

# Start the Flask app when the container starts
CMD ["python", "app.py"]