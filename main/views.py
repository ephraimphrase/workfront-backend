from django.shortcuts import render
from .serializers import GigSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Gigs
from rest_framework.views import APIView

# Create your views here.
class GigsList(generics.ListCreateAPIView):
    queryset = Gigs.objects.all()
    serializer = GigSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class GigDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gigs.objects.all()
    serializer = GigSerializer