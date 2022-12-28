### Description

An Instagram Influencer search portal built with Fastapi.
### How to run locally
* Download this repo or run... 
```bash
    $ git clone https://www.github.com/kayprogrammer/instagram-influencers/
```

In the root directory:

- Create a virtual environment, activate and run... `
```bash
    $ pip install -r requirements.txt`
```

- Create a .env file and copy all variables from the .env.example to the file.
    You can create a new database locally with pgadmin and input the details to the respected variables in the .env file. Like this...

    * SECRET_KEY = any unique random string
    * POSTGRES_USER = your postgres username
    * POSTGRES_PASSWORD = your postgres password
    * POSTGRES_DB = your postgres database name
    * PG_HOST = localhost
    * PG_PORT = 5432

## From terminal

- Start the server... 
```bash
    $ uvicorn setup.main:app --reload
```

# Run tests
    - Auth routes - 
    ```bash
        $ pytest apps/auth/tests.py --disable-warnings
    ```
    - Influencers routes - 
    ```bash
        $ pytest apps/influencers/tests.py --disable-warnings
    ```

## With Docker + Makefile
    - Change the value of POSTGRES_DB in .env file to postgres-db
    - Run to build container
    ```bash
        $ docker compose up --build -d --remove-orphans
    ``` 
    OR 
    ```bash
        $ make build to build container
    ```
    - Run to view logs 
    ```bash
        $ docker compose logs
    ``` 
    OR 
    ```bash
        $ make show-logs
    ```

# Run tests
    - Auth routes - 
    ```bash
        $ docker compose exec api pytest apps/auth/tests.py --disable-warnings
    ```
    OR
    ```bash
       $ make test-auth
    ```

    - Influencers routes - 
    ```bash
        $ docker compose exec api pytest apps/influencers/tests.py --disable-warnings
    ```
    OR
    ```bash
        $ make test-influencers
    ```

### Endpoints
- Docs: /docs/ 
- Auth 
    * Register: /api/v1/auth/register
    * Login: /api/v1/auth/login
    * Refresh token: /api/v1/auth/refresh
    * Logout: /api/v1/auth/logout

- Influencers
    * Provide details: /api/v1/influencers/provide-details
    * Search: /api/v1/influencers/search
