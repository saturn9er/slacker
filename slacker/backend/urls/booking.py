from django.urls import path

from backend.views import booking

urlpatterns = [
    path('', booking.index, name='booking-index'),
    # path('<int:guest_id>/', guests.detail, name='booking-detail'),
    path('create/', booking.BookingCreateView.as_view(), name='booking-create'),
    path('<int:pk>/edit/', booking.BookingUpdateView.as_view(), name='booking-edit'),
    # path('autocomplete/', guests.guests_autocomplete, name='guest-autocomplete'),
]