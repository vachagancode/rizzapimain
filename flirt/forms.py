from django.forms import ModelForm
from .models import Senetence

class AddFlirtForm(ModelForm):
    class Meta:
        model = Senetence
        fields = "__all__"