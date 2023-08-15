from django.shortcuts import render
from .serializers import GigSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Gigs
from rest_framework.views import APIView
from django.contrib.auth.models import User

# Create your views here.
class GigView(APIView):
    def post(self, request):
        gigName = request.data.get('gigName')
        gigCategory = request.data.get('gigCategory')
        gigDuration = request.data.get('gigDuration')
        clientName = request.data.get('clientName')
        gigAmount = request.data.get('gigAmount')
        paymentType = request.data.get('paymentType')
        startingAmount = request.data.get('startingAmount')
        gigType = request.data.get('gigType')

        try:
            gig = Gigs.objects.create(gigName=gigName, gigCategory=gigCategory, gigDuration=gigDuration, clientName=clientName, gigAmount=gigAmount, paymentType=paymentType, startingAmount=startingAmount,gigType=gigType, owner=request.user)
            gig.save()

            serializer = GigSerializer(gig)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"error":"An error occured"}, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request):
        gig = Gigs.objects.filter(owner=request.owner)
        serializer = GigSerializer(gig)

        return Response(serializer.data)
    
class GigDetail(APIView):
    def post(self, request, pk):
        gig = Gigs.objects.get(id=pk)
        serializer = GigSerializer(gig, data=request.data)

        if serializer.is_valid:
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request, pk):
        gig = Gigs.objects.get(id=pk)
        serializer = GigSerializer(gig)

        return Response(serializer.data, status=status.HTTP_200_OK)
