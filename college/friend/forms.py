from django.forms import modelform_factory
from .models import func1
from django import forms
class func1(forms.Form):
    class meta:
       firstname=forms.CharField(max_length=200)
       lastname=forms.CharField(max_length=200)
