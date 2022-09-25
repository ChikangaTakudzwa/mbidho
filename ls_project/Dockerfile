FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED=1
WORKDIR /livesounds

ADD requirements.txt /livesounds/requirements.txt
RUN pip3 install -r requirements.txt

ADD . /livesounds

# CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]

