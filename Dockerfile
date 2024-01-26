FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the Python script and requirements file
COPY app.py .
COPY requirements.txt .

# Create a directory for data and copy data into the container
RUN mkdir -p /tmp/data
COPY data/* /tmp/data/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port
EXPOSE 8080

# Command to run the application
CMD ["python", "app.py"]
