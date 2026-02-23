FROM python:3.12-slim
EXPOSE 8000
RUN mkdir -p /app
WORKDIR /app 
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
ENTRYPOINT ["python3"] 
CMD ["manage.py", "runserver", "0.0.0.0:8000"]