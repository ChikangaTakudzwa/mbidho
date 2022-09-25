FROM python:3.8.13
ENV PYTHONUNBUFFERED=1
WORKDIR /livesounds

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . /livesounds

# CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]

