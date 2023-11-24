FROM python:3.12.0

WORKDIR /app

COPY . /app

ENV PYTHONUNBUFFERED=1

RUN pip3 install -r requirements.txt

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8500"]

#docker run -p 8000:8000 my-django-app
