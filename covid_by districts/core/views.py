from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import View


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST request!')


home_page = HomeView.as_view()
