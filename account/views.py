from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny

# Create your views here.
class CustomTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)

class CustomTokenRefreshView(TokenRefreshView):
    permission_classes = (AllowAny,)

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

            serializer = UserSerializer(user)

            refresh = RefreshToken.for_user(user)
            token = str(refresh.access_token)
            
            return Response({'token': token, 'message':serializer.data, 'refresh':refresh}, status=status.HTTP_201_CREATED)
