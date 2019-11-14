from django.urls import path

from backend.views import rooms

urlpatterns = [
    path('', rooms.index, name='rooms-index'),
    path('<int:room_id>/', rooms.detail, name='rooms-detail'),
    path('<int:room_id>/status/', rooms.update_room_status, name='room-status-update'),
    path('<int:room_id>/note/', rooms.post_room_note, name='post-room-note'),
]