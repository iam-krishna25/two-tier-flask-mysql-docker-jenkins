# Two-Tier Flask + MySQL App with Docker & Jenkins

This project is a simple two-tier web application:

- **Frontend/Backend:** Flask (Python)
- **Database:** MySQL
- **DevOps:** Docker, Docker Compose, Jenkins, GitHub
- **Environment:** AWS EC2

## Features

- Shows a list of products from MySQL.
- Form to add a new product.
- Containerized using Docker.
- Jenkins pipeline builds, pushes, and deploys the app to EC2.

## Run locally

```bash
docker-compose up --build
# open http://localhost:5000
```

## CI/CD Flow

1. Push code to GitHub.
2. Jenkins is triggered.
3. Jenkins:
   - Checks out code
   - Builds and tests
   - Builds Docker image and pushes to Docker Hub
   - SSHs into EC2 and runs `docker-compose up -d --build`

Update the `Jenkinsfile` with your:
- Docker Hub username
- EC2 public IP
- GitHub repo URL
