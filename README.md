# Fast Quotes

## Install dependencies

This project uses [poetry](https://python-poetry.org/) for managing dependencies.

```
poetry install
```

## Run

```
uvicorn fast_quotes.main:app --reload
```

## Call the API

Note: Examples using [HTTPie](https://httpie.io/)

```
# Add Quote
http POST http://localhost:8000/quote who=ben what=random when=today where=BBC

# Get Random Quote
http http://localhost:8000/quote
```

## Lint

```
poetry run pylint
```

## Code Style

```
poetry run pycodestyle fast_quotes/main.py
```

## Running with Docker

This project supports Docker, providing an easy and consistent way to deploy the application. Ensure you have Docker installed on your system before proceeding. You can download and install Docker from [the official website](https://www.docker.com/products/docker-desktop).

#### Build the Docker Image

1. Navigate to the root directory of the project where the `Dockerfile` is located.
2. Build the Docker image using the following command. Replace `fast-quotes` with your preferred image name:

```bash
docker build -t fast-quotes .
```

This command creates a Docker image named `fast-quotes` based on the instructions in the `Dockerfile`.

#### Run the Docker Container

After building the image, you can start a container from it:

```bash
docker run -d --name fast-quotes-container -p 8000:8000 fast-quotes
```

This command runs a container named `fast-quotes-container` in detached mode, maps port 8000 of the container to port 8000 on your host, allowing you to access the FastAPI application via `http://localhost:8000`.

#### Verify the Application is Running

You can verify that the application is running and accessible by opening your web browser and navigating to:

```
http://localhost:8000/health
```

You should see a JSON response indicating the application status, such as `{"STATUS": "OK"}`.

#### Stopping and Removing the Container

When you're done, you can stop the container using:

```bash
docker stop fast-quotes-container
```

And if you wish to remove the container:

```bash
docker rm fast-quotes-container
```