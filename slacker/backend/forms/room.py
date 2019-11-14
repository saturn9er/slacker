from django.forms import ModelForm, TextInput, EmailInput, TimeInput, DateInput, Textarea, Select
from backend.models import Room


class StatusForm(ModelForm):
    class Meta:
        model = Room
        fields = ['status']
        widgets = {
            'status': Select(attrs={'class': 'select'}),
        }
