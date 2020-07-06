from __future__ import unicode_literals
import json
import uuid
from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.core import serializers

def fillup_username(request):
    game_id = request.POST['game_id']
    person = request.POST['person']
    m = models.tiktactoe.objects.get(linker=game_id)
    if m.first_player is None:
        m.first_player = person
    else:
        if m.first_player == person:
            pass
        else:
            m.second_player = person  
    m.save()
    return HttpResponse('Done')

def game_screen(request, game_id):
    return render(request, 'screen.html', {'game_id': game_id}) 

def create_new_game(request):
    m = models.tiktactoe.objects.create()
    print(m)
    return HttpResponse(m.linker)

def move(request):
    game_id = request.POST['game_id']
    m = models.tiktactoe.objects.get(linker=game_id)
    user = request.POST['user']
    sm_nos = request.POST['sm_nos']
    symbol = '' 
    if m.first_player == user:
        symbol = 'cross'
    else:
        symbol = 'circle'
    lnk = models.game.objects.create(link=m, user=user, sm_nos=sm_nos, symbol=symbol)
    lnk.save()
    context = {
        'user': user,
        'sm_nos': sm_nos,
        'symbol': symbol
    }
    data = json.dumps(context, indent=4, sort_keys=True, default=str)
    return HttpResponse(data, content_type='application/json')

def previous_data(request):
    game_id = request.POST['game_id']
    m = models.tiktactoe.objects.get(linker=game_id)
    main = models.game.objects.filter(link=m)
    data = serializers.serialize('json', main)
    return HttpResponse(data)