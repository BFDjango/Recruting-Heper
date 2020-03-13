from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from recruting.main.models import MyUser
from recruting.main.serializers import MyUserSerializer


class RegistrationView(APIView):
    def post(self, request):
        passwd = request.data.get('password')
        usr = request.data.get('username')
        serializer = MyUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        my_user = MyUser.objects.get(username=usr)
        my_user.set_password(passwd)
        my_user.save()
        return Response(serializer.data)

