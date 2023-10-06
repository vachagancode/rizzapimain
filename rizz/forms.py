from django import forms
from .models import Rizz

class RizzCreationForm(forms.ModelForm):
    class Meta:
        model = Rizz
        fields = "__all__"