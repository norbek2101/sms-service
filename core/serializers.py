from rest_framework import serializers

class SendSmsSerializer(serializers.Serializer):
    phone_number = serializers.IntegerField()
    text = serializers.CharField(max_length=256)