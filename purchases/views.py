from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView
from . import models
from users import models as user_models
from ipware import get_client_ip
from django.contrib.gis.geoip2 import GeoIP2
from django.shortcuts import render, HttpResponse
import os


import requests

# Create your views here.


class HomeView(ListView):
    """ HomeView Definition """

    model = models.Purchase
    template_name = "home.html"
    context_object_name = "purchases"

    def get(self, request):
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        client_id = os.environ.get("KAKAO_MAP_KEY")

        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")

        g = GeoIP2()

        return render(request, "home.html", {
            "ip": ip,
       
        }) 



def Participate(request):
    model = models.Purchase
    user = request.user
    model.participants.add(user)
