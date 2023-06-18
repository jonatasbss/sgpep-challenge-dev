FROM python:3.8.10

WORKDIR /sgpe

COPY requirements-dev.txt .

RUN pip install -r requirements-dev.txt

COPY . .

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE sgpe.settings

RUN python manage.py migrate

CMD python manage.py runserver 0.0.0.0:8000