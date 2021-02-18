from django import forms
from .models import Alert


class AlertForm(forms.ModelForm):

    class Meta:
        model = Alert
        fields = ['message', 'asset_id', 'min_value', 'max_value']