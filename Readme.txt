Steps to run:
    1. docker build -t sheet_loader .
    2. docker-compose up -d
    3. docker-compose exec sheet_loader python sheet_loader/manage.py migrate


Environments_variables for local dev:
    export POSTGRES_DB=postgres
    export POSTGRES_USER=postgres
    export POSTGRES_PASSWORD=postgres
    export POSTGRES_HOST=localhost
    export POSTGRES_PORT=5434
    export GOOGLE_SHEET_CREDS=/utils/google/creds/credentials.json
