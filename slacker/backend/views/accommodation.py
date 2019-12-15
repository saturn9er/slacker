from django.core.paginator import Paginator
from django.db.models import Q, Sum
from django.shortcuts import HttpResponseRedirect, get_object_or_404, render
from django.utils import timezone
from django.views.decorators.http import require_POST

from backend.models import Accommodation, Guest, Payment, Room
from backend.services.accommodation import *


def index(request):

    number_of_rows_on_a_page = 10
    accommodations = get_paginated_accommodations(request, number_of_rows_on_a_page)

    context = { 'accommodations': accommodations }

    return render(request, 'accommodation/index.html', context)



def create(request):

    room = get_room_or_404(request)

    context = { 'room': room }

    return render(request, 'accommodation/create.html', context)



@require_POST
def check_in(request):

    room = get_room_or_404(request)
    accommodation = create_accommodation(request, room)

    process_payment(request, accommodation)
    add_new_guests_to_accommodation(request, accommodation)
    set_room_occupied(room, accommodation)

    redirect_url = request.POST.get('next', '')

    return HttpResponseRedirect(redirect_url)



def check_out(request, accommodation_id):

    accommodation = get_object_or_404(Accommodation, pk=accommodation_id)
    accommodation.check_out = timezone.now()
    accommodation.save()

    set_room_vacant(accommodation)

    return HttpResponseRedirect('/')



def detail(request, accommodation_id):

    accommodation = get_object_or_404(Accommodation, pk=accommodation_id)
    room = get_object_or_404(Room, pk=accommodation.room.id)
    guests = accommodation.guests.all()
    payments = Payment.objects.filter(accommodation=accommodation)
    total_paid = sum(payment.amount for payment in payments)

    context = { 'accommodation': accommodation, 'room': room,
               'guests': guests, 'payments': payments, 'total_paid': total_paid }

    return render(request, 'accommodation/detail.html', context)



def new_payment(request, accommodation_id):

    redirect = request.GET.get('next', '')

    accommodation = get_object_or_404(Accommodation, pk=accommodation_id)

    process_payment(request, accommodation)

    return HttpResponseRedirect(redirect)



def update_note(request, accommodation_id):

    redirect = request.GET.get('next', '')

    accommodation = get_object_or_404(Accommodation, pk=accommodation_id)
    accommodation.note = request.POST['note']
    accommodation.save()

    return HttpResponseRedirect(redirect)