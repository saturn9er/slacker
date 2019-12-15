from django.urls import path

from backend.views import accommodation

urlpatterns = [
    path('', accommodation.index, name='accommodation-index'),
    path('<int:accommodation_id>/', accommodation.detail, name='accommodation-detail'),
    path('create/', accommodation.create, name='accommodation-create'),
    path('check-in/', accommodation.check_in, name='accommodation-check-in'),
    path('<int:accommodation_id>/payment', accommodation.new_payment, name='accommodation-new-payment'),
    path('<int:accommodation_id>/check-out', accommodation.check_out, name='accommodation-check-out'),
    path('<int:accommodation_id>/note', accommodation.update_note, name='accommodation-note-update')
]