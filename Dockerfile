FROM python:3.8

WORKDIR /sheet_loader

RUN pip install pipenv

COPY . .

RUN pipenv install --system --deploy

#CMD python sheet_loader/manage.py runserver 0.0.0.0:80
