from django.shortcuts import render
from .models import Portfolio, Services
# Create your views here.
def home(request):
    serob = Services.objects.all()
    portob = Portfolio.objects.all()
    context = {'serob': serob, 'portob': portob,}
    return render(request, 'home/index.html', context)
 
