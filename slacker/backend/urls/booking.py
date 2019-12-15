from django.urls import path

from backend.views import booking

urlpatterns = [
    path('', booking.index, name='booking-index'),
    path('create/', booking.BookingCreateView.as_view(), name='booking-create'),
    path('<int:pk>/edit/', booking.BookingUpdateView.as_view(), name='booking-edit')
]