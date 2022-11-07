# EAtHome Server

FastAPI + PostgreSQL

## Development API Server

```sh
pdm run dev
```

## Database

### Start PostgreSQL Docker Container

```sh
docker-compose up
```

### Run Migration

```sh
pdm run migrate -m "description"
```

> If a new model is added, the model should be imported in `migrations/env.py`

### Upgrade Database

```sh
pdm run push_db
```
