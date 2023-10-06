from rest_framework import serializers
from .models import Rizz

class RizzSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rizz
        fields = '__all__'