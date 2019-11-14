from django.shortcuts import render, get_object_or_404, reverse, HttpResponseRedirect
from django.views.decorators.http import require_POST
from backend.models import Guest, Accommodation, Payment
from backend.forms.room import StatusForm
from django.utils import timezone
from django.contrib import messages
from datetime import datetime

# Create your views here.


def get_guest_blank(request):
    guest_id = request.GET['guest_id']
    accommodation_id = request.GET['accommodation_id']

    guest = get_object_or_404(Guest, pk=guest_id)
    accommodation = get_object_or_404(Accommodation, pk=accommodation_id)

    context = {'guest': guest, 'accommodation': accommodation}
    return render(request, 'report/guest_blank.html', context)


def shift_report_index(request):
    if request.GET.get('date'):
        period = request.GET.get('date')
        dates = period.split(' - ')
        datetimes = []

        for date in dates:
            date = datetime.strptime(date + ' 8:00:00', '%Y-%m-%d %H:%M:%S')
            datetimes.append(date)
            print(date)

        payments = Payment.objects.filter(made_on__range=datetimes).order_by(
            'accommodation__room__id', 'accommodation')

        cash_sum = 0
        pos_sum = 0
        bank_sum = 0

        for payment in payments:
            if payment.payment_type == Payment.CASH:
                cash_sum += payment.amount
            elif payment.payment_type == Payment.POS:
                pos_sum += payment.amount
            elif payment.payment_type == Payment.BANK_TRANSFER:
                bank_sum += payment.amount

        sum = {'cash': cash_sum, 'pos': pos_sum, 'bank': bank_sum}

        context = {'payments': payments, 'start': datetimes[0], 'end': datetimes[1], 'sum': sum}

        return render(request, 'report/shift.html', context)
    else:
        return render(request, 'report/shift_index.html')