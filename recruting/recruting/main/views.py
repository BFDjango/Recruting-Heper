import logging

from django.contrib import auth
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework import generics, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from recruting.main.models import MyUser
from recruting.main.serializers import MyUserFullSerializer
logger = logging.getLogger('log')


class RegistrationView(APIView):
    def post(self, request):
        passwd = request.data.get('password')
        usr = request.data.get('username')
        serializer = MyUserFullSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        my_user = MyUser.objects.get(username=usr)
        my_user.set_password(passwd)
        my_user.save()
        logger.info(f"{self.request.user} registered into the system")
        logger.warning(f"{self.request.user} registered into the system")
        logger.error(f"{self.request.user} registered into the system")
        logger.critical(f"{self.request.user} registered into the system")
        return Response(serializer.data)


@csrf_exempt
def logout(request):
    user = auth.logout(request)
    return JsonResponse({'message': 'logged out'}, status=status.HTTP_200_OK)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MyUserFullSerializer
    # permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return MyUser.objects.all()

    @action(methods=['GET'], detail=False)
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)