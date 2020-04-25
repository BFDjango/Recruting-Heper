import json
import logging

from django.contrib import auth
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from recruting.main.models import MyUser
from recruting.main.serializers import MyUserSerializer

logger = logging.getLogger('log')


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
        Response(serializer.data)
        logger.info(f"{self.request.user} registered into the system")
        logger.warning(f"{self.request.user} registered into the system")
        logger.error(f"{self.request.user} registered into the system")
        logger.critical(f"{self.request.user} registered into the system")


# class ChangePasswordAPIView(APIView):
#     # permission_classes = (IsAuthenticated,)
#
#     def put(self, request):
#         user = MyUser.objects.get(username=request.user.username)
#         new_password = self.request.data.pop('new_password')
#         user.set_password(new_password)
#         user.save()
#         return Response({}, status=status.HTTP_200_OK)


@csrf_exempt
def logout(request):
    user = auth.logout(request)
    return JsonResponse({'message': 'logged out'}, status=status.HTTP_200_OK)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MyUserSerializer
    # permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return MyUser.objects.all()

    @action(methods=['GET'], detail=False)
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)




