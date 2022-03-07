from django.forms import modelform_factory
from.models import next
from django import forms
class next(forms.Forms):
    class meta:
        age=forms.IntegerField(max_length=30)
        firstname=forms.CharField(max_length=30)
        lastname=forms.CharField(max_length=15)
