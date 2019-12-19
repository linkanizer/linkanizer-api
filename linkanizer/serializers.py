from rest_framework import serializers

from .models import Link, List


class ListSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    name = serializers.CharField()

    class Meta:
        model = List
        fields = ("id", "name", "created", "modified", "owner")


class LinkSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    title = serializers.CharField()
    url = serializers.URLField()

    list = serializers.PrimaryKeyRelatedField(
        queryset=List.objects.all(), write_only=True
    )

    class Meta:
        model = Link
        fields = ("id", "title", "url", "list", "created", "modified", "owner")
