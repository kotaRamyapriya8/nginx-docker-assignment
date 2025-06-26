#  Nginx Reverse Proxy with Docker Compose

This project demonstrates a simple microservices setup using Docker Compose, Nginx as a reverse proxy, and two backend services — one built with Flask (Python) and another with FastAPI (Python).

---

##  Project Structure
nginx-docker-assignment/
├── docker-compose.yml
├── nginx/
│   ├── nginx.conf
│   └── Dockerfile
├── service_1/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── service_2/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
└── README.md


 1. Clone the Repository

git clone https://github.com/YourGitHubUsername/nginx-docker-assignment.git
cd nginx-docker-assignmen

1. Run the Application

docker compose up --build
This will start all services using bridge networking and route requests via Nginx.


3.Features

Docker Compose setup for multi-container system

Nginx reverse proxy with path-based routing

Clean, modular Dockerfiles

Fast startup and automatic dependency installa/tion
