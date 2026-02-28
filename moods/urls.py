from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('ayah/<str:mood_name>/',views.ayah_by_mood),
]