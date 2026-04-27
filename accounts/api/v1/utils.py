import threading
from django.core.mail import send_mail
import time

class EmailThread(threading.Thread):
    def __init__(self, email_object):
        threading.Thread.__init__(self)
        self.email_object = email_object

    def run(self):
        self.email_object.send(fail_silently=False)

