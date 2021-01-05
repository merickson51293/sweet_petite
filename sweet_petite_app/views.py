from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.db.models import Sum


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
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['email']
            try:
                send_mail(name, subject, message, from_email, ['sweetpetitedes@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('/success')
    return render(request, "contact_form.html", {'form': form})

def success(request):
    return render(request, "success.html")

def blog(request):
    context={
        'blogs':Blog.objects.all
    }
    return render(request, "blog.html", context)

def checkout(request):
    last = Order.objects.last()
    price=last.total_price
    full_order = Order.objects.aggregate(Sum('quantity_ordered'))['quantity_ordered__sum']
    full_price = Order.objects.aggregate(Sum('total_price'))['total_price__sum']
    context = {
        'orders':full_order,
        'total':full_price,
        'bill':price,
    }
    return render(request, "store/checkout.html",context)

def purchase(request):
    if request.method == 'POST':
        this_product = Goods.objects.filter(id=request.POST["id"])
        if not this_product:
            return redirect('/')
        else:
            quantity = int(request.POST["quantity"])
            total_charge = quantity*(float(this_product[0].price))
            Order.objects.create(quantity_ordered=quantity, total_price=total_charge)
            return redirect('/checkout')
    else:
        return redirect('/')