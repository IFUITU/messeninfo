from rest_framework import serializers
from .models import Branchen

class BranchenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branchen
        fields = ("id", 'text',)