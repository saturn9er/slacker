from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.decorators.http import require_POST
from backend.models import Room, RoomType, RoomNote, Accommodation
from backend.forms.room import StatusForm
from django.utils import timezone
from django.contrib import messages


def index(request):
    rooms_list = Room.objects.all()
    room_types_list = RoomType.objects.all()

    info = {
        'total_rooms': rooms_list.count(),
        'occupied_rooms': rooms_list.filter(status=Room.OCCUPIED).count(),
        'empty_rooms': rooms_list.filter(status=Room.EMPTY).count(),
        'cleaning_rooms': rooms_list.filter(status=Room.CLEANING).count(),
        'repair_rooms': rooms_list.filter(status=Room.REPAIR).count(),
    }

    context = {'rooms': rooms_list, 'room_types': room_types_list, 'info': info}
    
    return render(request, 'rooms/index.html', context)


def detail(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    status_form = StatusForm()
    notes = RoomNote.objects.filter(room_id=room.id).order_by('-created_at')[:50]
    recent_accommodations = Accommodation.objects.filter(room_id=room.id).order_by('-id')[:50]
    context = {'room': room, 'status_form': status_form, 'notes': notes, 'recent_accommodations': recent_accommodations}
    return render(request, 'rooms/detail.html', context)


@require_POST
def update_room_status(request, *args, **kwargs):
    redirect = request.GET['next']

    room_id = request.POST['room_id']
    status = request.POST['status']

    room = get_object_or_404(Room, pk=room_id)
    room.status = status
    room.status_changes_at = timezone.now
    room.save()

    messages.success(request, '')

    return HttpResponseRedirect(redirect)

@require_POST
def post_room_note(request, *args, **kwargs):
    redirect = request.GET['next']

    room_id = request.POST['room_id']
    room = get_object_or_404(Room, pk=room_id)
    user = request.user
    content = request.POST['content']

    room_note = RoomNote(content=content, created_by=user, room=room)
    room_note.save()

    return HttpResponseRedirect(redirect)
