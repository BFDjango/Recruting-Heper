from django.urls import path

from recruting.message.views import ChatListAPIView

urlpatterns = [
    path('chat/', ChatListAPIView.as_view()),
]