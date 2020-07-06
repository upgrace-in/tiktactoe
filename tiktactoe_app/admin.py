# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models

class moveadmin(admin.TabularInline):
    model = models.game

@admin.register(models.tiktactoe)
class tiktactoe_admin(admin.ModelAdmin):
    inlines = [
        moveadmin
    ]