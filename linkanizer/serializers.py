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
    url = serializers.URLField(required=True)
    imageUrl = serializers.URLField(read_only=True)
    description = serializers.CharField(read_only=True)
    visits = serializers.IntegerField(read_only=True)

    order = serializers.IntegerField(read_only=True)

    list_id = serializers.PrimaryKeyRelatedField(read_only=True)
    list = serializers.PrimaryKeyRelatedField(
        queryset=List.objects.all(), write_only=True
    )

    class Meta:
        model = Link
        fields = (
            "id",
            "title",
            "url",
            "list",
            "list_id",
            "created",
            "modified",
            "owner",
            "order",
            "imageUrl",
            "description",
            "visits",
        )
