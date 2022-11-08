# EAtHome Server

FastAPI + PostgreSQL

## Development API Server

```sh
pdm run dev
```

## Database

### Start PostgreSQL + pgAdmin Docker Container

```sh
docker compose up
```

- PostgreSQL Default Settings
  - Hostname: db
  - Port: 5432
  - Database: postgres
  - Username: postgres
  - Password: changeme
- pgAdmin Default Settings
  - URL: http://localhost:5050
  - Email: pgadmin4@pgadmin.org
  - Password: admin

### Run Migration

```sh
pdm run migrate -m "description"
```

> If a new model is added, the model should be imported in `migrations/env.py`

### Apply Migrations to Database

```sh
pdm run push_db
```
