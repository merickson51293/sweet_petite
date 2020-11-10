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