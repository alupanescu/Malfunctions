from django.db import models
from django.forms import forms


class Malfunction(models.Model):
    name= models.CharField(max_length=200, null=False)
    location=models.CharField(max_length=300, null=False)
    explanation=models.CharField(max_length=500, null=False)
    img_upload = models.ImageField(upload_to='img/', null=True)
    file_upload = models.FileField(upload_to='files/', null=True)









