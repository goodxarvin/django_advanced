from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from time import sleep
from django.core.cache import cache
import requests
from .tasks import celery_send_email


def send_mail(request):
    celery_send_email.delay()
    return HttpResponse("<h1>email sent</h1>")


headers = {
    "Accept": "application/json"
}

proxies = {
    "http": "http://host.docker.internal:10808",
    "https": "http://host.docker.internal:10808",
}



def test(request):
    if not cache.get("get_test_api"):
        response = requests.get("https://61c70ce0-ce7f-45bb-b697-6cdb0609ed75.mock.pstmn.io/test/sleep/5",
        proxies=proxies,)
        cache.set("get_test_api", response.json())
    # print(response.__dict__)
    return JsonResponse(cache.get("get_test_api"))