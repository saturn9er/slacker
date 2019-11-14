from django.urls import path

from backend.views import report

urlpatterns = [
    path('blank/', report.get_guest_blank, name='reports-blank'),
    path('shift/', report.shift_report_index, name='reports-shift-index')
]