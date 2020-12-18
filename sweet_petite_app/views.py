from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm


def index(request):
    context={
        'goods':Goods.objects.all()
    }
    return render(request, "index.html", context)

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

# def contact(request):
#     return render(request, "contact.html")

def order(request):
    context={
        "goods":Goods.objects.all
    }
    return render(request, "order.html", context)

def menu(request):
    context={
        "goods":Goods.objects.all
    }
    return render(request, "menu.html", context)



def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['sweetpetitedes@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('/success')
    return render(request, "contact_form.html", {'form': form})

def success(request):
    return HttpResponse('Success! Thank you for your message.')

def blog(request):
    context={
        'blogs':Blog.objects.all
    }
    return render(request, "blog.html", context)