from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Mood, Ayah
import requests
import random

@api_view(['GET'])
def ayah_by_mood(request, mood_name):
    mood = Mood.objects.get(name=mood_name)
    ayahs = Ayah.objects.filter(mood=mood)
    random_ayah = random.choice(list(ayahs))
    
    url = f"http://api.alquran.cloud/v1/ayah/{random_ayah.surah_no}:{random_ayah.ayah_no}/en.asad"
    response = requests.get(url)
    data = response.json()
    
    return Response({
        'mood': mood_name,
        'arabic': data['data']['text'],
        'translation': data['data']['edition']['englishName'],
    })