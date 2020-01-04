from rest_framework import serializers

from .models import Link, List


class ListSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    name = serializers.CharField()
    order = serializers.IntegerField(read_only=True)

    class Meta:
        model = List
        fields = ("id", "name", "created", "modified", "owner", "order")


class LinkSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    title = serializers.CharField()
    url = serializers.URLField()
    order = serializers.IntegerField(read_only=True)

    list = serializers.PrimaryKeyRelatedField(
        queryset=List.objects.all(), write_only=True
    )

    class Meta:
        model = Link
        fields = ("id", "title", "url", "list", "created", "modified", "owner", "order")
