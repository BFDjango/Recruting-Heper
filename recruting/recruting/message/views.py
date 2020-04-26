import logging

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import ChatSerializer
from .models import Chat

logger = logging.getLogger('log')


@api_view(['GET', 'POST'])
def chatting(request):
    if request.method == 'GET':
        usr = request.user
        mess = Chat.objects.filter(to_mes=usr)
        serializer = ChatSerializer(mess, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ChatSerializer(data=request.data)
        from_mes = request.user
        if serializer.is_valid():
            serializer.save(from_mes=from_mes)
            # logger.info(f"{self.request.user} bla bla bla")
            # logger.warning(f"{self.request.user} bla bla bla")
            # logger.error(f"{self.request.user} bla bla bla")
            # logger.critical(f"{self.request.user} bla bla bla")
            return Response(serializer.data)
        return Response(serializer.errors)