from rest_framework import serializers
from .models import Senetence

class SentenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Senetence
        fields = "__all__"