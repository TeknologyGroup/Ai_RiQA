FROM python:3.9-slim-buster

RUN apt-get update && apt-get install -y gfortran

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]
