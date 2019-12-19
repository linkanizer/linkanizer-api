from django_filters import rest_framework as filters

from .models import Link, List


def lists(request):
    if request is None:
        return List.objects.none()

    return request.user.lists.all()


class LinkFilter(filters.FilterSet):
    list = filters.ModelChoiceFilter(queryset=lists)

    class Meta:
        model = Link
        fields = ("list",)
