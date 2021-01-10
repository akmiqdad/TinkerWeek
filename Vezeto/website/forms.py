from django import forms
from .models import Participent

class RegForm(forms.ModelForm):

    class Meta:
        model = Participent
        fields = ('name','institute_name','year','email','phone','event')