from django.shortcuts import render
from .models import ContentE,ContentM

# Create your views here.

def home(request):
    return render(request, 'home.html')

def index(request):
    contentE = ContentE.objects.all()
    return render(request, 'index.html', {'contentE': contentE})

def indexM(request):
    contentM = ContentM.objects.all()
    return render(request, 'indexM.html', {'contentM': contentM})
