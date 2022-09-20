from platform import node
from pyexpat import model
from django.db import models
import uuid

# Create your models here.
class Services(models.Model):
    Title = models.TextField(null=True, blank=False)
    description = models.TextField(null=True, blank=False)
    icon = models.ImageField(upload_to="img/%y", null=True)

class Portfolio(models.Model):
    title = models.TextField(null=True, blank=False)
    subtitle = models.TextField(null=True, blank=False)
    image1 = models.ImageField(upload_to="img/%y", null=True)
    image2 = models.ImageField(upload_to="img/%y", null=True)
    desc =  models.TextField(null=True, blank=False)
    link = models.TextField(null=True, blank=False)
