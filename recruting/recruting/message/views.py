import logging

from rest_framework import generics, viewsets, status, mixins
from recruting.message.models import Chat
from recruting.message.serializers import ChatSerializer

logger = logging.getLogger('log')


class ChatListAPIView(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      generics.GenericAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    # permission_classes = (IsAuthenticated)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.create(request, *args, **kwargs)
        logger.info(f"{self.request.user} started the chat")
        logger.warning(f"{self.request.user} started the chat")
        logger.error(f"{self.request.user} started the chat")
        logger.critical(f"{self.request.user} started the chat")








