from django.forms import ModelForm, TextInput, EmailInput, TimeInput, DateInput, Textarea, Select
from backend.models import Booking


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['number', 'number_of_guests', 'status', 'check_in', 'check_out', 'guest_name',
                  'price', 'note', 'room_type', 'source']
        widgets = {
             'number': TextInput(attrs={'class': 'input'}),
             'number_of_guests': TextInput(attrs={'class': 'input', 'value': '1', 'min': '1', 'max': '3', 'style': 'max-width: 50px; text-align: center;', 'readonly': ''}),
             'price': TextInput(attrs={'class': 'input'}),
             'check_in': DateInput(attrs={'class': 'input date', 'type': 'text', 'placeholder': '22.05.2019'}),
             'check_out': DateInput(attrs={'class': 'input date', 'type': 'text', 'placeholder': '29.05.2019'}),
             'guest_name': TextInput(attrs={'class': 'input'}),
             'note': Textarea(attrs={'class': 'textarea', 'rows': '4'}),
        }
