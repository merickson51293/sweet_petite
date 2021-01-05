from django.db import models
import re

class ReviewManager(models.Manager):
    def validator (self, postdata):
        errors={}
        if len(postdata['name'])<2:
            errors['name']="Name must be longer than 2 characters!"
        if len(postdata['review'])<5:
            errors['review']="Review must be longer than 5 characters!"
        return errors

class Review(models.Model):
    name=models.CharField(max_length=55)
    review=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=ReviewManager()

class Goods(models.Model):
    name=models.CharField(max_length=255)
    price=models.IntegerField()
    description=models.CharField(max_length=255)
    picture=models.ImageField(upload_to ='imgs/')
    best_seller=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.name}"

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    message = models.TextField(max_length=400)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Blog(models.Model):
    title=models.CharField(max_length=255)
    post=models.TextField()
    picture=models.ImageField(upload_to='imgs/')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Order(models.Model):
    quantity_ordered = models.IntegerField()
    total_price = models.DecimalField(decimal_places=2, max_digits=6)
    description = models.TextField()
    goods = models.ForeignKey(Goods, related_name="order_goods", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    