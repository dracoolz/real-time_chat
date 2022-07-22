from datetime import *
from django.utils import timezone
from django.db import models
from datetime import datetime

# Create your models here.
#room id name
class Room(models.Model):
    name = models.CharField(max_length=1000)

#message
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=timezone.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)