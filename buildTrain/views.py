from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import StationForm


def home(request):
    return render(request, 'buildTrain/home.html')

def select_hand(request):
    return render(request, 'buildTrain/select.html')

def select_station(request):

    if request.method == 'POST':
        form = StationForm(request.POST)
    
        if form.is_valid():
            return HttpResponseRedirect('buildTrain/')
    
    else:
        form = StationForm()
    
    return render(request, 'buildTrain/station.html',  {'form': form })

def build_train(request, starter, hand):

    return render(request, 'buildTrain/build.html')
