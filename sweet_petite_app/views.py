from django.shortcuts import render, redirect
from .models import *

def index(request):
    return render(request, "index.html")

def reviews(request):
    context={
        'reviews': Review.objects.all()
    }
    return render(request, "reviews.html", context)

def add_review(request):
    review = Review.objects.create(name=request.POST["name"], review=request.POST['review'])
    return redirect('/reviews')

def photos(request):
    return render(request, "photos.html")

def celebrations(request):
    return render(request, "celebrations.html")

def graduation(request):
    return render(request, "graduation.html")

def misc(request):
    return render(request, "misc.html")

def contact(request):
    return render(request, "contact.html")

def order(request):
    return render(request, "order.html")

def menu(request):
    context={
        "goods":Goods.objects.all
    }
    return render(request, "menu.html", context)