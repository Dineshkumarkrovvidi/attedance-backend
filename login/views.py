from django.shortcuts import render
from .models import LoginModel
from rest_framework import viewsets
from .serializer import LoginSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.
# class LoginView(viewsets.ModelViewSet):
#     queryset=LoginModel.objects.all()
#     serializer_class=LoginSerializer
@api_view(['POST'])
def loginauth(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = LoginModel.objects.filter(username=username, password=password).first()
    
    if user:
        refresh = RefreshToken.for_user(user)
        return Response({
            "message": "Login successful",
            "access": str(refresh.access_token),
            "refresh": str(refresh)
        })
    else:
        return Response({"error": "Invalid username or password"}, status=400)
