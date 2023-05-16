from django import forms
from django.forms import TextInput, NumberInput, EmailInput, Textarea, DateInput, Select

from report_a_malfunction.models import Malfunction


class MalfunctionForm(forms.ModelForm):
    class Meta:
        model = Malfunction
        fields = ['name', 'location', 'explanation']

        widgets = {
            'name': TextInput(attrs={'placeholder': 'What kind of fault have you found?', 'class': 'form-control'}),
            'location': TextInput(attrs={'placeholder': 'Location', 'class': 'form-control'}),
            'explanation': TextInput(attrs={'placeholder': 'More details', 'class': 'form-control'}),

        }
