# Use the Python base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the application code to the container
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port on which your FastAPI application will run
EXPOSE 8000

# Start the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]