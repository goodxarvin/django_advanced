from django.shortcuts import render
from django.http import HttpResponse
from time import sleep
from .tasks import celery_send_email

def send_mail(request):
    celery_send_email.delay()
    return HttpResponse("<h1>email sent</h1>")