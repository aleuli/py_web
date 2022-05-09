from random import random

from datetime import datetime

from django.views import View
from django.http import HttpRequest, HttpResponse


class DateTimeView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        now = datetime.now()
        return HttpResponse(now)


class RandomViev(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        random_number = random()
        return HttpResponse(random_number)
