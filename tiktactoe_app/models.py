from __future__ import unicode_literals

from django.db import models
import uuid

class tiktactoe(models.Model):
    linker = models.CharField(max_length=200)

class game(models.Model):
    link = models.ForeignKey(tiktactoe, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)
    move = models.IntegerField(default=0)
    symbol = models.CharField(max_length=100)
