from django.urls import path
from . import views

urlpatterns=[
    path('', views.index),
    path('reviews', views.reviews),
    path('add_review', views.add_review)
]