from rest_framework import serializers
from moods.models import Mood, Ayah

class MoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mood
        fields = '__all__'

class AyahSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ayah
        fields = '__all__'