# Use the official Python image from the Docker Hub
FROM python:3.12
# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application directory into the container
COPY . .

# Create the directories for uploads and compressed files
RUN mkdir -p uploads compressed

# Set permissions for the uploads and compressed directories
RUN chmod -R 755 uploads compressed

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Set environment variables for Flask
ENV FLASK_APP=app/app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the Flask app
CMD ["flask", "run"]
