FROM python:3.12-slim
RUN useradd -u 1000 -m appuser
USER appuser
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


ENV HTTP_PROXY=http://22.25.234.183:8080
ENV HTTPS_PROXY=http://22.25.234.183:8080


EXPOSE 8000
WORKDIR /app 
COPY . .
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
