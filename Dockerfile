FROM python:3.8-slim-bullseye  

WORKDIR /app

COPY . /app

RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get update -y --fix-missing && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir awscli && \
    pip install --no-cache-dir -r requirements.txt

CMD ["python3", "app.py"]
