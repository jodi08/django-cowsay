from django import forms
from bossyapp.models import Bossy

class BossyInput(forms.Form):
    bossy = forms.CharField(max_length=250)