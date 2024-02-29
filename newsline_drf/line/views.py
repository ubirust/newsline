from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Note
from .serializers import NoteSerializer


# Create your views here.
class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
