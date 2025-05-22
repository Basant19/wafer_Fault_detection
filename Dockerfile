FROM python:3.12-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc g++ gfortran libatlas-base-dev libblas-dev liblapack-dev python3-dev meson ninja-build \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip setuptools wheel


RUN pip install -r requirements.txt

CMD ["python3", "app.py"]
