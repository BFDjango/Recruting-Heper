from rest_framework import serializers

from recruting.message.models import Chat


class ChatSerializer(serializers.ModelSerializer):
    from_mes = serializers.CharField(required=True)
    to_mes = serializers.CharField(required=True)
    mess = serializers.CharField(required=True)

    class Meta:
        model = Chat
        fields = ('id', 'from_mes', 'to_mes', 'mess', 'date')

