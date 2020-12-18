from django.urls import path
from . import views

urlpatterns=[
    path('', views.index),
    path('reviews', views.reviews),
    path('add_review', views.add_review),
    path('photos', views.photos),
    path('celebrations', views.celebrations),
    path('graduation', views.graduation),
    path('misc', views.misc),
    path('menu', views.menu),
    path('contact', views.contact),
    path('success', views.success),
    path('order', views.order),
    path('blog', views.blog),
]