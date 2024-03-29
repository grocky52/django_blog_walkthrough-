from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default= timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

# used by create and update views to get back to url created and or updated by the user
    def get_absolute_url(self):
        return reverse('blog:post-detail', kwargs={'pk': self.pk})


    #tittle author date_posted content
