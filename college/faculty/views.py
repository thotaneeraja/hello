from django.shortcuts import render,redirect
from.models import add
def home(request):
    emp=add.objects.all()
    return render(request,'home.html',{'emp':emp})

# Create your views here.
