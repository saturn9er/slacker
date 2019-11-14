from django.urls import path

from backend.views import guests

urlpatterns = [
    path('search/', guests.search, name='guests-search'),
    path('<int:guest_id>/', guests.detail, name='guests-detail'),
    path('create/', guests.GuestCreateView.as_view(), name='guest-create'),
    path('<int:pk>/update/', guests.GuestUpdateView.as_view(), name='guest-edit'),
    path('autocomplete/', guests.guests_autocomplete, name='guest-autocomplete'),
]