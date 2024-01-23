from django.shortcuts import render
from .models import Sliders, Proje, Yonetim, Idare, SastisDevam, Galeri
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings


def home(request):
    data = {
        "sliders": Sliders.objects.all,
        "proje": Proje.objects.all,
        "yonetim": Yonetim.objects.all,
        "idare": Idare.objects.all,
        "satis": SastisDevam.objects.all,
        "galeri": Galeri.objects.all,
    }

    return render(request, "index.html", data)


