from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.utils import timezone

from backend.models import Room, Accommodation, Payment

def get_paginated_accommodations(request, number_of_rows_on_a_page):

    accommodation_list = Accommodation.objects.order_by('-id')

    page = request.GET.get('page')
    paginator = Paginator(accommodation_list, number_of_rows_on_a_page)

    return paginator.get_page(page)



def get_room_or_404(request):

    room_id = request.GET['room_id']
    
    return get_object_or_404(Room, pk=room_id)



def create_accommodation(request, room):

    cost = request.POST['cost']
    accommodation_type = request.POST['accommodation_type']
    note = request.POST['note']
    accommodation_quantity = request.POST['accommodation_quantity']

    accommodation = Accommodation()
    accommodation.cost = cost
    accommodation.accommodation_type = accommodation_type
    accommodation.note = note
    accommodation.room = room
    accommodation.accommodation_quantity = accommodation_quantity
    accommodation.save()

    return accommodation



def process_payment(request, accommodation):
    
    payment_type = request.POST['payment_type']
    amount = request.POST['amount']

    payment = Payment()
    payment.payment_type = payment_type
    payment.amount = amount
    payment.accommodation = accommodation
    payment.save()

    return payment



def add_new_guests_to_accommodation(request, accommodation):

    guests = request.POST.getlist('guest')

    for guest_id in guests:
        if int(guest_id or 0) > 0:
            guest = get_object_or_404(Guest, pk=guest_id)
            guest.last_visit = timezone.now()
            guest.save()
            accommodation.guests.add(guest)



def set_room_occupied(room, accommodation):

    room.current_accommodation = accommodation
    room.status = Room.OCCUPIED
    room.status_changed_at = timezone.now()
    room.save()



def set_room_vacant(accommodation):

    room = accommodation.room
    room.current_accommodation = None
    room.status = Room.CLEANING
    room.status_changed_at = timezone.now()
    room.save()