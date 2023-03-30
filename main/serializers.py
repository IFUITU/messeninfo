from rest_framework import serializers
from .models import Branchen, Btom, Messe

class BranchenSerializer(serializers.ModelSerializer):
    # big_img = serializers.ImageField()
    # small_img = serializers.ImageField()

    class Meta:
        model = Branchen
        fields = ("id", 'text','b_id',)


class MesseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messe
        fields = "__all__"

class BtomSerializer(serializers.ModelSerializer):
    messe = MesseSerializer()
    class Meta:
        model = Btom
        fields = "__all__"
        depth = 1
    