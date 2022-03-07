from django.shortcuts import render,redirect
from.models import func1
from.forms import modelform_factory
from django import forms
def login(request):
    emp=func1.objects.all()
    return render(request,'login.html',{'emp':emp})

# Create your views here.
