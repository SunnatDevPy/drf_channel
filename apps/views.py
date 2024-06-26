from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Message
from .serializer import MessageSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
