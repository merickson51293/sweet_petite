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
