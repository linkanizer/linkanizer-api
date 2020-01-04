from rest_framework import serializers


class RequestLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    class Meta:
        fields = ("email",)


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()

    class Meta:
        fields = ("email",)
