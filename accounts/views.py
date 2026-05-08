from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from time import sleep
from django.views.decorators.cache import cache_page
import requests
from .tasks import celery_send_email


def send_mail(request):
    celery_send_email.delay()
    return HttpResponse("<h1>email sent</h1>")


proxies = {
    "http": "http://host.docker.internal:10808",
    "https": "http://host.docker.internal:10808",
}


@cache_page(60) # ---> parameter to set the timeout
def test(request):
    # if not cache.get("get_test_api"):
    response = requests.get("https://61c70ce0-ce7f-45bb-b697-6cdb0609ed75.mock.pstmn.io/test/sleep/5",
    proxies=proxies,)
        # cache.set("get_test_api", response.json(), 60) --> second parameter defines after how long the cache will updates itself.
    # print(response.__dict__)
    return JsonResponse(response.json())