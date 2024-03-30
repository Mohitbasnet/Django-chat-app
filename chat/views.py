from django.shortcuts import render

import json

from django.http import JsonResponse

from django.views.decorators.http import require_POST

from . models import Room

from django.contrib.auth.decorators import login_required

from account.models import User

from account.forms import AddUserForm

@require_POST
def create_room(request, uuid):
    name = request.POST.get('name','')
    url = request.POST.get('url', '')


    Room.objects.create(uuid = uuid, client = name, url =url)

    return JsonResponse({'message': 'room created'})


@login_required

def admin(request):
    rooms = Room.objects.all()
    users = User.objects.filter(is_staff=True)

    return render(request, 'chat/admin.html',{
        'rooms': rooms,
        'users': users
    })


@login_required
def room(request, uuid):
    room = Room.objects.get(uuid = uuid)
    return render(request, 'chat/room.html',{
        'room': room
    })


@login_required
def add_user(request):
    form = AddUserForm()

    return render(request,'chat/add_user.html',{
        'form': form
    })

