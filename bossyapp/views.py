from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse
from bossyapp import forms
from bossyapp.forms import BossyInput
from bossyapp.models import Bossy
import subprocess


# Create your views here.
#Need to take in cowsays and display a form to input what bossy should say. Return a blank form with input in bossy's word bubble.


def index_view(request):
    bossy_says = ""
    if request.method == "POST":
        form = forms.BossyInput(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Bossy.objects.create(input=data.get("bossy"))
            bossy_says = subprocess.run(["cowsay", data.get('bossy')], capture_output=True, text=True)
            bossy_says = bossy_says.stdout
    form = BossyInput()
    return render(request, 'index.html', {'form':form, 'bossy_says': bossy_says})

def history_view(request):
    """Helped by Sohail"""
    history = Bossy.objects.filter().order_by('-id')[:10]
    return render(request, 'recent.html', {'history': history})
