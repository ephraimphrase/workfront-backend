from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
import jwt
from datetime import datetime, timedelta
from django.conf import settings



# Create your views here.
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SignUpView(APIView):
    def post(self, request):
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email = request.data.get('email')
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or password:
            return Response({'error': 'Username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            User.objects.get(username=username)
            return Response({'error': 'Username already exists.'}, status=status.HTTP_400_BAD_REQUEST),
        except User.DoesNotExist:
            user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.save()

            serializer = UserSerializer(data=user)

            # Generate JWT token
            expiration_time = datetime.utcnow() + timedelta(hours=1)
            payload = {'user_id': user.id, 'username': user.username, 'exp':expiration_time}
            token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

            return Response({'token': token, 'message':serializer.data}, status=status.HTTP_201_CREATED)


class SignInView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if not user:
            return Response({'error': 'Invalid username or password.'}, status=status.HTTP_401_UNAUTHORIZED)
        
        login(request, user)

        # Generate JWT token
        expiration_time = datetime.utcnow() + timedelta(hours=1)
        payload = {'user_id': user.id, 'username': user.username, 'exp':expiration_time}
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

        return(Response({'token':token}, status=status.HTTP_200_OK))
