from django.shortcuts import render,redirect
from.models import next
def signup(request):
    emp=next.objects.all()
    return render(request,'signup.html',{'emp':emp})

# Create your views here.
