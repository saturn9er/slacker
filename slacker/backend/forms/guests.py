from django.forms import ModelForm, TextInput, EmailInput, TimeInput, DateInput, Textarea, Select
from backend.models import Guest


class GuestForm(ModelForm):
    class Meta:
        model = Guest
        fields = ['last_name', 'first_name', 'patronymic', 'sex', 'home_address', 'date_of_birth', 'place_of_birth', 'document_type',
                  'document_number', 'document_issued_by', 'document_issued_on', 'phone', 'email', 'note']
        widgets = {
            'last_name': TextInput(attrs={'class': 'input'}),
            'first_name': TextInput(attrs={'class': 'input'}),
            'patronymic': TextInput(attrs={'class': 'input'}),
            'home_address': TextInput(attrs={'class': 'input'}),
            'date_of_birth': DateInput(attrs={'class': 'input date', 'placeholder': '08.10.1999'}),
            'place_of_birth': TextInput(attrs={'class': 'input'}),
            'document_type': Select(attrs={'class': 'select'}),
            'document_number': TextInput(attrs={'class': 'input'}),
            'document_issued_by': TextInput(attrs={'class': 'input'}),
            'document_issued_on': DateInput(attrs={'class': 'input date', 'placeholder': '12.11.2013'}),
            'phone': TextInput(attrs={'class': 'input phone', 'type': 'tel', 'placeholder': '+7(999)000-00-00'}),
            'email': EmailInput(attrs={'class': 'input', 'type': 'email'}),
            'note': Textarea(attrs={'class': 'textarea', 'rows': '4'}),
        }
