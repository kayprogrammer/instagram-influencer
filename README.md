<p align="center">
  <a href="https://fastapi.tiangolo.com"><img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI"></a>
</p>

---

## Description

A simple Instagram Influencer search portal built with Fastapi.

## How to run locally

* Download this repo or run: 
```bash
    $ git clone https://www.github.com/kayprogrammer/instagram-influencers/
```

In the root directory:
---
- Create a virtual environment, activate and run...
```bash
    $ pip install -r requirements.txt
```
- Create a file `.env` and copy all variables from the `.env.example` to the file.
    You can create a new database locally with pgadmin and input the details to the respected variables in the .env file. Like this...

    * SECRET_KEY=any_unique_random_string
    * POSTGRES_USER=your_postgres_username
    * POSTGRES_PASSWORD=your_postgres_password
    * POSTGRES_DB=your_postgres_database_name
    * PG_HOST=localhost
    * PG_PORT=5432

- Start the server... 
```bash
    $ uvicorn setup.main:app --reload
```

#### Test Coverage
---
- Auth routes 
```bash
    $ pytest apps/auth/tests.py --disable-warnings
```
- Influencers routes 
```bash
    $ pytest apps/influencers/tests.py --disable-warnings
```

### With Docker + Makefile
---
- Change the value of POSTGRES_DB in `.env` file from localhost to postgres-db
- Run command below to build container
```bash
    $ docker compose up --build -d --remove-orphans
``` 
OR 
```bash
    $ make build
```
- Run command below to view logs 
```bash
    $ docker compose logs
``` 
OR 
```bash
    $ make show-logs
```

#### Test Coverage
---
- Auth routes
```bash
    $ docker compose exec api pytest apps/auth/tests.py --disable-warnings
```
OR
```bash
    $ make test-auth
```

- Influencers routes
```bash
    $ docker compose exec api pytest apps/influencers/tests.py --disable-warnings
```
OR
```bash
    $ make test-influencers
```

## Endpoints

- Docs
    * Swagger: `/docs` 
- Auth 
    * Register: `/api/v1/auth/register`
    * Login: `/api/v1/auth/login`
    * Refresh token: `/api/v1/auth/refresh`
    * Logout: `/api/v1/auth/logout`

- Influencers
    * Provide details: `/api/v1/influencers/provide-details`
    * Search: `/api/v1/influencers/search`
