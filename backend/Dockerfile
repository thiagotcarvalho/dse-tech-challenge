FROM python:3.8-slim

RUN apt-get update
RUN apt-get install -y --no-install-recommends libpq-dev gcc python3-dev
RUN rm -rf /var/lib/apt/lists/*
WORKDIR /app/backend
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]