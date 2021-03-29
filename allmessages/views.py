from django.shortcuts import render, redirect
from django.contrib import messages
from .models import AllMessages
from datetime import datetime
import re


def index(request):
    mess = AllMessages.objects.all()
    return render(request, "index.html", {'mess': mess})


def create(request):
    if request.method == "POST":
        email = request.POST["email"]
        message = request.POST["message"]
        todaytime = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
            if 0 < len(message) < 100:
                AllMessages.objects.create(
                    email=email,
                    message=message,
                    create_date=todaytime,
                    update_date=todaytime
                )
                return redirect("/")
            else:
                messages.info(request, "Invalid message")
                return redirect("create")
        else:
            messages.info(request, "Invalid email")
            return redirect("create")
    else:
        return render(request, "create.html")


def update(request, link):
    if request.method == "POST":
        email = request.POST["email"]
        message = request.POST["message"]
        todaytime = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
            if 0 < len(message) < 100:
                AllMessages.objects.filter(id=link).update(
                    email=email,
                    message=message,
                    update_date=todaytime
                )
                return redirect("/")
            else:
                messages.info(request, "Invalid message")
                mes = AllMessages.objects.get(id=link)
                return render(request, "update.html", {'mes': mes})
        else:
            messages.info(request, "Invalid email")
            mes = AllMessages.objects.get(id=link)
            return render(request, "update.html", {'mes': mes})
    else:
        mes = AllMessages.objects.get(id=link)
        return render(request, "update.html", {'mes': mes})


def single(request, link):
    mes = AllMessages.objects.get(id=link)
    return render(request, "single.html", {'mes': mes})


def lists(request, link):
    start = int(link + "0")
    stop = int(link + "9") + 1
    mess = AllMessages.objects.all()[start:stop]
    return render(request, "lists.html", {'mess': mess})
