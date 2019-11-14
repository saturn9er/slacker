from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import (HttpResponseRedirect, get_object_or_404, render,
                              reverse)
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView

from backend.forms.booking import BookingForm
from backend.models import Booking


def index(request):
    booking_list = Booking.objects.exclude(status = Booking.CHECKED_IN).order_by('check_in')
    paginator = Paginator(booking_list, 20)
    page = request.GET.get('page')
    bookings = paginator.get_page(page)
    context = {'bookings': bookings}
    return render(request, 'booking/index.html', context)

class BookingCreateView(SuccessMessageMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'booking/create.html'
    context_object_name = "booking"
    success_message = "Успешно создано!"

class BookingUpdateView(SuccessMessageMixin, UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = 'booking/edit.html'
    context_object_name = "booking"
    success_message = "Успешно сохранено!"
