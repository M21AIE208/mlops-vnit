#define the base image
FROM python:3.11-slim

WORKDIR /app

#this will copy requirements.txt from the current directory to the /app directory in the container
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5004

CMD ["python", "app.py"]