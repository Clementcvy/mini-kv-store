# mini-kv-store

1. Project's goals

Little backend service that permits to stock, to fetch and to delete couples key-value

2. planned endpoints

PUT     /v1/kv/{key}    create or update a value
GET     /v1/kv/{key}    fetch a value
DELETE  /v1/kv/{key}    delete a value 
GET     /health         check if the service answers

3. Data model

table : kv_items
key TEXT PRIMARY KEY
value TEXT NOT NULL
created_at TIMESTAMPTZ NOT NULL
updated_at TIMESTAMPTZ NOT NULL

4. What does the MVP contain

- a HTTP server that starts
- a db PostgreSQL connected
- PUT /v1/kv/{key} to store a value
- GET /v1/kv/{key} to fetch a value
- DELETE /v1/kv/{key} to delete a value
- clean errors
- some tests
- Docker Compose
- a simple README

5. What's intentionally excluded

- memory cache
- authentication
- replication
- Kubernetes
- advanced benchmark
- custom TCP protocol
- dashboard
- full monitoring

6. Use of the app

- cp .env.example .env

