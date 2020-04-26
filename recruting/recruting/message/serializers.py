from rest_framework import serializers

from recruting.message.models import Chat


class ChatSerializer(serializers.Serializer):
    from_mes = serializers.CharField(required=True)
    to_mes = serializers.CharField(required=True)
    mess = serializers.CharField(required=True)
    date = serializers.DateTimeField(required=False)

    class Meta:
        model = Chat
        fields = ('id', 'from_mes', 'to_mes', 'mess', 'date')

    def create(self, validated_data):
        return Chat.objects.create(**validated_data)

    def update(self, instance, validated_data):
        pass