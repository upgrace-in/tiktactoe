"""tiktactoe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from django.views.generic import TemplateView
from tiktactoe_app import views

urlpatterns = [
    path('previous_data/', views.previous_data, name="previous_data"),
    path('fillup_username/', views.fillup_username, name="fillup_username"),
    path('new_game/<str:game_id>/', views.game_screen, name="screen"),
    path('create_new_game/', views.create_new_game, name="create_new_game"),
    path('move/', views.move, name="move"),
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="index.html"), name="index"),
]
