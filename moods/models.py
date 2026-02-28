from django.db import models

# Create your models here.

class Mood(models.Model):
    name = models.CharField(max_length=100)

class Ayah(models.Model):
    surah_no = models.IntegerField()
    ayah_no = models.IntegerField()
    mood = models.ForeignKey(Mood,on_delete=models.CASCADE)