# mini-kv-store

1. Project overview

mini-kv-store is a small backend project. It is a simple key-value store where a user can create, fetch, update, and delete values by key. The data is stored in PostgreSQL.

I developed this project to better understand how a clean backend project can be built using Python, FastAPI, Docker, PostgreSQL, Git, tests, and CI.

2. Features

- Create or update a key-value pair
- Fetch a value using its key
- Delete a key-value pair using its key
- Store data in PostgreSQL
- Run the project with Docker Compose
- Unit and integration tests
- Continuous integration with GitHub Actions
- Project configuration with `pyproject.toml`

3. Tech stack

- **Language:** Python
- **Version control:** Git / GitHub
- **Backend:** FastAPI
- **Database:** PostgreSQL
- **Database driver:** psycopg
- **Testing:** pytest
- **Containerization:** Docker
- **CI:** GitHub Actions

4. Architecture

The application follows a simple layered backend architecture. Each layer has a clear responsibility.

```text
Client
  -> FastAPI routes
  -> Service layer
  -> Repository layer
  -> PostgreSQL
```

The API layer exposes REST endpoints using FastAPI.
The service layer contains the business rules and transaction boundaries.
The repository layer handles SQL queries using psycopg.
PostgreSQL stores the data.

For more details, see `docs/architecture.md`.

5. Data model

A table named `kv_items` is used to store the key-value pairs. The table is created only if it does not already exist.

```sql
CREATE TABLE IF NOT EXISTS kv_items (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

- `key` is the primary key. It is used to create, read, update, and delete a pair.
- `value` stores the value linked to the key.
- `created_at` is set when the pair is created.
- `updated_at` is updated when the value is changed.

6. API endpoints

- `GET /health`: checks if the API is running.

```bash
curl http://localhost:8000/health
```

It returns `{"status": "ok"}`.

- `PUT /v1/kv/{key}`: creates or updates a key-value pair.

```bash
curl -X PUT http://localhost:8000/v1/kv/name \
  -H "Content-Type: application/json" \
  -d '{"value":"Alice"}'
```

It returns `{"key":"name","value":"Alice"}`.

- `GET /v1/kv/{key}`: gets an existing key-value pair.

```bash
curl http://localhost:8000/v1/kv/name
```

It returns `{"key":"name","value":"Alice"}` if the key exists.

- `DELETE /v1/kv/{key}`: deletes an existing key-value pair.

```bash
curl -X DELETE http://localhost:8000/v1/kv/name
```

It returns no body when the delete succeeds.

7. Run locally

```bash
git clone https://github.com/Clementcvy/mini-kv-store
cd mini-kv-store
cp .env.example .env
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
docker compose up -d postgres
uvicorn kvstore.main:app --reload
```

Once finished, stop Uvicorn with `Ctrl + C`, then stop PostgreSQL:

```bash
docker compose down
```

To also remove the PostgreSQL volume and reset the database:

```bash
docker compose down -v
```

8. Run with Docker Compose

```bash
git clone https://github.com/Clementcvy/mini-kv-store
cd mini-kv-store
docker compose up --build
```

Once finished, stop the app with `Ctrl + C`, then run:

```bash
docker compose down
```

To also remove the PostgreSQL volume and reset the database:

```bash
docker compose down -v
```

9. Tests

pytest is used to write and run automated tests for the Python code.

Unit tests check individual parts of the code:

```bash
pytest tests/unit
```

Integration tests check the application with PostgreSQL. Start PostgreSQL first:

```bash
docker compose up -d postgres
```

Then run:

```bash
pytest tests/integration
```

You can also run the full stack with:

```bash
docker compose up --build
```

When finished:

```bash
docker compose down
```

Ruff is used to lint and format-check the Python code:

```bash
ruff check src tests
```

It should return `All checks passed!`.

10. CI

The CI is divided in two:

- `quality-and-unit-tests`: runs Ruff and unit tests.
- `integration-tests`: starts PostgreSQL, initializes the database, and runs integration tests.

This is used to check that the project still works on every push and pull request.

11. Logs

Logs are used to record important events and errors in the application to make monitoring and debugging easier.

`logging_config.py` defines the log format and the log level. Example:

```text
2026-09-14 17:06:40,921 level=INFO kvstore.main event=application_started
```

In `main.py`, an `INFO` log is sent when an operation succeeds. A `WARNING` log is sent for client errors, and an `ERROR` log is sent for database errors.

12. Limitations

- memory cache
- authentication
- replication
- Kubernetes
- advanced benchmark
- custom TCP protocol
- dashboard
- complete monitoring

13. Future improvements

- Add authentication
- Add request rate limiting
- Add metrics endpoint
- Add connection pooling
- Add TTL support for keys
- Add an optional in-memory cache
