from django.shortcuts import render
from django.views import View
from django.http import HttpRequest, HttpResponse


class CommonView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        com_now = """<h1>Hello, World</h1>"""
        return HttpResponse(com_now)


class IndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'common/index.html')
