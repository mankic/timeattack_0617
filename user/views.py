from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions  # 권한 설정
from rest_framework.response import Response

from django.contrib.auth import login, authenticate, logout

from user.models import User,UserType

class SingUp(APIView):
    permission_classes = [permissions.AllowAny]

    # 회원가입
    def post(self, request):
        email = request.data.get('email', '')
        password = request.data.get('password', '')
        type = request.data.get('type','')

        type = UserType.objects.get(type=type)
        
        User(email=email, password=password, type=type).save()

        return Response({"message": "signup success!!"})