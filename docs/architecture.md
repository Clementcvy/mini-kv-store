# Architecture

1. Overview

This document describes the architecture of the application, the responsibilities
of its main components, and the main technical decisions made during development.

2. High-Level Architecture

```text
Client
  -> FastAPI routes
  -> Service layer
  -> Repository layer
  -> PostgreSQL
```

3. Project Structure

```text
src/kvstore/
├── main.py
├── config.py
├── db.py
├── logging_config.py
├── repository.py
├── service.py
└── schemas.py

tests/
├── unit/
└── integration/
```

4. Layers

The API layer is responsible for receiving HTTP requests, validating input and returning HTTP responses.

Service Layer
The service layer contains the application's business rules. It coordinates operations between the API and the persistence layer.

Data Access Layer
The data access layer contains database queries. Database communication is handled using psycopg.

Database
PostgreSQL is used as the relational database.

5. Request Flow

A typical request follows this path:

```text
HTTP Request
    ↓
FastAPI Route
    ↓
Input Validation
    ↓
Service
    ↓
Repository
    ↓
PostgreSQL
    ↓
Repository
    ↓
Service
    ↓
FastAPI Response
```

6. Testing Architecture

Tests are implemented using pytest.
Unit tests validate individual components.
Integration tests validate interactions with the database and API.
Tests are automatically executed by GitHub Actions.

7. Infrastructure
Docker is used to provide consistent development and testing environments.
The application and PostgreSQL database can be started using Docker containers.
GitHub Actions runs the continuous integration pipeline on every push or pull request.

8. Design Decisions

Why FastAPI?
FastAPI was selected because it provides:
- automatic request validation
- automatic OpenAPI documentation
- simple REST API development
- good integration with Python type annotations

Why PostgreSQL?
PostgreSQL provides a reliable relational database with strong support for
transactions and structured data.

Why separate services and repositories?
Separating business logic from database access improves:
- testability
- maintainability
- separation of concerns
