from __future__ import unicode_literals

from django.db import models
import uuid

class tiktactoe(models.Model):
    linker = models.CharField(max_length=200, default=uuid.uuid4)
    first_player = models.CharField(max_length=100, null=True, blank=True)
    second_player = models.CharField(max_length=100, null=True, blank=True)
    
class game(models.Model):
    link = models.ForeignKey(tiktactoe, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)
    sm_nos = models.CharField(max_length=100)
    symbol = models.CharField(max_length=100)
