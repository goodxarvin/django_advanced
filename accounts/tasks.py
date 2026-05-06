from celery import shared_task
from time import sleep 

@shared_task
def celery_send_email():
    sleep(3)
    print("email sent successfully")