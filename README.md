# store_admin_py_ws

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Running the App](#running-the-app)
- [Test](#test)
- [Docker](#docker)
  - [Image Resource Usage Metrics](#image-resource-usage-metrics)
- [Kubernetes](#kubernetes)
  - [Pod Resource Usage Metrics](#pod-resource-usage-metrics)

## Description

Store's Admin Web Service example using [Django](https://www.djangoproject.com/) framework.

## Installation

```bash
$ pip install -r requirements.txt
```

## Running the app
The following commands allow you to run the application

```bash
# development
$ python manage.py runserver
```

### Swagger API documentation
You can access the Swagger documentation at `/swagger` path, ie: `http://localhost:3040/swagger`

## Test

```bash
python manage.py test
```

## Docker

```bash
# Build Docker image
docker build -t store_admin_py_ws:latest -f Dockerfile .

# Run Docker container (with example port mappings and environment variables)
docker run -p 3040:3040 -p 5432:5432 -e SERVER_PORT="3040" -e DB_HOST="host.docker.internal" -e DB_PORT="5432" -e DB_USERNAME="postgres" -e DB_PASSWORD="1234" -e DB_NAME="sale-management-system" store_admin_py_ws
```

### Image resource usage metrics

The table below shows resource usage metrics for the `store-admin-ws` Docker container.

| REPOSITORY           | TAG    | IMAGE ID      | CREATED      | SIZE  |
|----------------------|--------|---------------|--------------|-------|
| store-admin-py-ws    | latest | ea98a671f394  | 2 hours ago  | 200MB |


## Kubernetes

```bash
# Start Minikube to create a local Kubernetes cluster
minikube start

# Configure the shell to use Minikube's Docker daemon
& minikube -p minikube docker-env --shell powershell | Invoke-Expression

# Build Docker image with a specific tag and Dockerfile
docker build -t store-admin-py-ws:latest -f Dockerfile .

# Apply Kubernetes configuration to create a pod
kubectl apply -f kubernetes/pod.yaml

# Port-forward to access the Kubernetes pod locally
kubectl port-forward store-admin-py-ws-pod 3040:3040
```

### Pod resource usage metrics

The table below shows resource usage metrics for the `store-admin-ws-pod` pod.

```bash
minikube addons enable metrics-server
kubectl top pods
```

**Note:** If you just enabled the metrics-server addon, remember to wait a couple of seconds before running the `kubectl top pods` command.


| NAME                | CPU(cores) | MEMORY(bytes) |
|---------------------|------------|---------------|
| store-admin-ws-pod  | 1m         | 91Mi          |
