FROM python:3.8.0
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD python fargate_task.py
