from django.shortcuts import render,redirect
from.models import disp

def index(request):
    emp=disp.objects.all()
    return render(request,'index.html',{'emp':emp})

# Create your views here.
