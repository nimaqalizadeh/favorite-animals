# Django Animal Management App

## Overview

This Django application is designed to manage animals with user authentication and CRUD (Create, Read, Update, Delete) functionalities. It uses PostgreSQL as the database and is containerized with Docker for both the backend and the database.

## Getting Started

### Prerequisites

- **Docker**: Ensure Docker is installed on your machine.
- **Docker Compose**: Make sure Docker Compose is installed.

### Setup

1. **Clone the Repository**

   ```bash
   git clone git@github.com:nimaqalizadeh/manage-animals.git
   cd manage-animals
   ```

2. **Build and Start Containers**

   ```bash
   docker compose up --build
   ```

3. **Database Migrations**

The migrations are handeled in `Dockerfile` file.

## Application Usage


1. **User Registration and Authentication**

- Register: `/accounts/register`
- Login: `/accounts/login`
- Logout: `/accounts/logout`

Register a new user, log in, and log out to manage your animal records.

2. **Animal Management**

After logging in, you can manage your animals through the following URL:

- View and Add Animals: `/animals/`

Use the form to add new animals. This operation is handled via AJAX.

3. **API Endpoints**

The application provides a RESTful API for managing animals (Only authenticated users can access this endpoint):

- List and Create Animals: `GET /animals/api/v1/list` and `POST /animals/api/v1/list`

- Read, Update, and Delete Animals: `GET /animals/api/v1/detail/<id>/`, `PUT /animals/api/v1/detail/<id>/`, `DELETE /animals/api/v1/detail/<id>/`

## License

This project is licensed under the MIT License.

Feel free to submit issues and pull requests to contribute to this project.
