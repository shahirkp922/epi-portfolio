from django.shortcuts import render
from .models import ContentE,ContentM

# Create your views here.

def home(request):
    return render(request, 'home.html')
# English content view
def index(request):
    contentE = ContentE.objects.all()
    return render(request, 'index.html', {'contentE': contentE, 'language': 'en'})  

# Malayalam content view
def indexM(request):
    contentM = ContentM.objects.all()
    return render(request, 'index.html', {'contentM': contentM, 'language': 'ml'})  
