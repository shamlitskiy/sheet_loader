Steps to run:
    1. Download creds .json from Service Account in Google Cloud:
        1. rename it to credentials.json
    2. pit it in the /utils/google/creds/ directory
    3. Build image, run it and apply migrations:
        1. docker build -t sheet_loader .
        2. docker-compose up -d
        3. docker-compose exec sheet_loader python sheet_loader/manage.py migrate
    4. open localhost:8080 in browser
    5. Press "Setup google sheet" and set google spreadsheet id and data range
    6. Press "Apply" button
    7. The table will update every 60 sec. If you want to update table press "Update table button".
