![Python Logo](https://www.python.org//static/img/python-logo.png)

# Image Compressor Web App

This is a Flask-based web application that allows users to upload images, compress them to a `.jpg` format, and then download the compressed image. The app is containerized using Docker for easy deployment.

## Features

- Upload images in `.png`, `.jpg`, or `.jpeg` formats
- Compress the images and convert them to `.jpg` format with reduced quality
- Download the compressed image
- Dockerized for easy deployment

## Tools and Technologies

- **Python**: Backend development
- **Flask**: Web framework for the app
- **Pillow (PIL)**: Python Imaging Library used for image compression
- **Docker**: Containerization of the app for consistent development and production environments
- **Tailwind CSS**: Frontend framework for styling

## Requirements

To run this project locally, you'll need the following installed:

- Python 3.x
- Docker
- Git

## How to Run Locally

### 1. Clone the Repository

To clone this project to your local machine, run:

```bash
git clone https://github.com/YogiCodersRealm/ImageCompressor.git
cd ImageCompressor ```

### 2. Build the Docker Image
In the root of the project directory, build the Docker image using the following command:

```bash
docker build -t image_compressor .
```

### 3 Run the Docker Container
To run the app in Docker, use this command:
```bash
docker run -p 5000:5000 -v $(pwd)/app/uploads:/app/uploads -v $(pwd)/app/compressed:/app/compressed image_compressor
```

This will bind the Flask app to localhost:5000, and mount the uploads and compressed directories to ensure files are saved in your local file system.

### 4. Access the App
Once the container is running, you can access the app by navigating to the following URL in your web browser:
```http://localhost:5000```




