FROM python:3.9-slim-buster

RUN apt-get update && apt-get install -y \
    gfortran \
    libopenblas-dev \
    liblapack-dev

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "backend.app:app", "--host", "0.0.0.0", "--port", "8000"]
