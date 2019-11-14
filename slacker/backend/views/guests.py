from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import (HttpResponseRedirect, get_object_or_404, render,
                              reverse)
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.views.generic.edit import CreateView, UpdateView

from backend.forms.guests import GuestForm
from backend.forms.room import StatusForm
from backend.models import Guest, Room, RoomNote, RoomType, Accommodation


def search(request):
    query = request.GET.get('query', '')
    guest_list = Guest.objects.filter(
        Q(last_name__icontains=query) | Q(document_number__contains=query) | Q(phone__contains=query)).order_by('-id')
    paginator = Paginator(guest_list, 15)
    page = request.GET.get('page')
    guests = paginator.get_page(page)
    context = {'guests': guests}
    return render(request, 'guests/search.html', context)


def detail(request, guest_id):
    guest = get_object_or_404(Guest, pk=guest_id)
    recent_accommodations = Accommodation.objects.filter(guests__id=guest.id).order_by('-id')[:50]
    context = {'guest': guest, 'recent_accommodations': recent_accommodations}
    return render(request, 'guests/detail.html', context)


class GuestCreateView(SuccessMessageMixin, CreateView):
    model = Guest
    form_class = GuestForm
    template_name = 'guests/create.html'
    context_object_name = "guest"
    success_message = "Успешно создано!"


class GuestUpdateView(SuccessMessageMixin, UpdateView):
    model = Guest
    form_class = GuestForm
    template_name = 'guests/update.html'
    context_object_name = "guest"
    success_message = "Успешно сохранено!"


def guests_autocomplete(request):
    query = request.GET.get('term', '')
    guests = Guest.objects.filter(
        Q(last_name__icontains=query) | Q(phone__contains=query) | Q(document_number__contains=query)).order_by('-id')[:10]
    results = []
    for guest in guests:
        guest_json = {}
        guest_json['id'] = guest.id
        guest_json['value'] = guest.fullname
        guest_json['label'] = "%s (%s)" % (guest.fullname, guest.document_number)
        guest_json['discount'] = guest.personal_discount
        results.append(guest_json)
    return JsonResponse(results, safe=False)
