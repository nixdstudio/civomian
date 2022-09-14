from django.db import models

# Create your models here.
#testsfd  
class Post(models.Model):
    image = models.FileField(blank=True)
    heading = models.CharField(max_length=200)
    content = models.TextField(max_length=1000)


class Mainpost(models.Model):
    image = models.FileField(blank=True)
    heading = models.CharField(max_length=200)
    content = models.TextField(max_length=1000)