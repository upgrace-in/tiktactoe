# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid
from django.shortcuts import render
from django.http import HttpResponse
from . import models

def screen(request, game_id):
    return render(request, 'screen.html', {'game_id': game_id}) 

def new_game(request):
    m = models.tiktactoe.objects.create(linker=uuid.uuid4)
    return screen(request, m.id)

def move(request):
    game_id = request.POST['game_id']
    m = models.tiktactoe.objects.get(id=game_id)
    user = request.POST['user']
    move = request.POST['move']
    symbol = request.POST['symbol']

    lnk = models.game.objects.create(link=m, user=user, move=move, symbol=symbol)
    lnk.save()
    context = {
        'user': user,
        'move': move,
        'symbol': symbol
    }
    data = json.dumps(context, indent=4, sort_keys=True, default=str)
    return HttpResponse(data, content_type='application/json')