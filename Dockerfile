FROM python:latest

WORKDIR /app
COPY . /app

RUN pip install Flask
CMD ["python3", "app.py"]
