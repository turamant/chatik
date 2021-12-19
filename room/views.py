from django.shortcuts import render

from .models import Room

# View for the rooms
def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'room/room_list.html', {'rooms': rooms})


def room(request, pk):
    room = Room.objects.get(pk=pk)

    return render(request, 'room/room_detail.html', {'room': room})