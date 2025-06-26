# Nginx Reverse Proxy with Docker Compose

This project demonstrates routing multiple services using Nginx as a reverse proxy with Docker Compose.

##  Stack
- Nginx
- Python Flask (Service 1)
- Python FastAPI (Service 2)
- Docker & Docker Compose
- Bridge Networking

##  Project Structure

nginx-docker-assignment/
├── docker-compose.yml
├── nginx/
│ ├── nginx.conf
│ └── Dockerfile
├── service_1/
│ ├── app.py (Flask app)
│ ├── requirements.txt
│ └── Dockerfile
├── service_2/
│ ├── app.py (FastAPI app)
│ ├── requirements.txt
│ └── Dockerfile
└── README.md


##  How It Works 

- Access Service 1 via: `http://<EC2_PUBLIC_IP>/service1`
- Access Service 2 via: `http://<EC2_PUBLIC_IP>/service2`

## Health Check 

Both services are exposed behind Nginx. Health checks can be validated using curl:

```bash
curl http://35.180.58.24  /service1  
curl http://35.180.58.24  /service2
 How to Run
SSH into EC2 and clone repo:

bash

git clone https://github.com/kotaRamyapriya8/nginx-docker-assignment.git
cd nginx-docker-assignment
Start containers:

bash

docker compose up --build
Visit:

http://<EC2_PUBLIC_IP>/service1

http://<EC2_PUBLIC_IP>/service2

 Ports
Make sure the EC2 Security Group allows:

HTTP (80)

SSH (22)

Custom TCP: 5001, 5002 (optional for direct testing)

 Author
Kota Ramyapriya
DevOps Intern | Azure + Docker + Linux
