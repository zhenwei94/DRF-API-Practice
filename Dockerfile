FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD . /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app

#CMD python manage.py runserver

RUN ./manage.py collectstatic --no-input

CMD gunicorn openshift_django.wsgi -b 0.0.0.0:3013

EXPOSE 3013

