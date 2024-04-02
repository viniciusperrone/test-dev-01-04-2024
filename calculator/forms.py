# forms.py
from django import forms
from .models import Consumer

class ConsumerForm(forms.ModelForm):
    class Meta:
        model = Consumer
        fields = ['name', 'document', 'zip_code', 'city', 'state', 'consumption', 'distributor_tax']
