# Use official Python image as base
FROM python:3.10

# Set working directory inside the container
WORKDIR /app

# Copy all files from your project directory to the container
COPY . /app

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 (Flask default)
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]
