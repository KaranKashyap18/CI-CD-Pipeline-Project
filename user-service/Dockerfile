FROM python:3.9-slim

WORKDIR /app

COPY user-service/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD ["python", "app.py"]  # Replace 'app.py' with your main script

