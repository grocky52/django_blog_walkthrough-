from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone

# Create your models here.

class post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default= timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    #tittle author date_posted content
