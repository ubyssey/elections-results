from django import forms
from .models import Race

class UpNextForm(forms.Form):
    race = forms.ModelChoiceField(queryset=Race.objects.all())

class CallRaceForm(forms.Form):
    race = forms.ModelChoiceField(queryset=Race.objects.all())
    results = forms.CharField(required=True)