# Django_Test

# Basic User Management API with Django Rest Framework

## Introduction

This is a basic API for user management developed using Django Rest Framework (DRF). The API is documented using DRF's built-in documentation tools along with the use of CoreAPI. Its core functionality revolves around performing CRUD operations for the `User` model.

The `User` model is defined as follows:

```python
from django.db import models

class User(models.Model):
    id = Auto Incremental
    name = Cadena de texto
    age = Numero positivo
    is_active = Booleano
    is_deleted = Booleano
    created_at = Fecha
    updated_at = Fecha
    deleted_at = Fecha
```
# Configuration
* Prerequisites
    * Docker installed on your system.
* Installation
    * Clone this repository to your local machine.
    * Navigate to the project directory.
# Usage
* To run this project, follow these steps:

    * Execute the following command to start the Docker containers:
        ```sh
            docker compose --file=./docker-compose.yml up
        ```
    * Once the Docker containers are up and running, you can interact with the API using HTTP requests.
# Endpoints
* GET /api/v1/users/: Retrieve a list of all users.
* GET /api/v1/users/{id}/: Retrieve details of a specific user.
* POST /api/v1/users/: Create a new user.
* PUT /api/v1/users/{id}/: Update an existing user.
* DELETE /api/v1/users/{id}/: Delete a user.
For detailed information about the API endpoints and their usage, refer to the API documentation.