from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import *
from .serializers import *


# Create your views here.
class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer


class AdvertisementViewSet(viewsets.ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer

    def get_queryset(self):
        user = self.request.query_params.get('user')
        if user:
            return Event.objects.filter(user=user).order_by('-timestamp')
        return Event.objects.none()