from django_filters import rest_framework as filters
from rest_framework import viewsets

from .filters import LinkFilter
from .serializers import LinkSerializer, ListSerializer


class LinkViewSet(viewsets.ModelViewSet):
    serializer_class = LinkSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = LinkFilter

    def get_queryset(self):
        return self.request.user.links.all()


class ListViewSet(viewsets.ModelViewSet):
    serializer_class = ListSerializer

    def get_queryset(self):
        return self.request.user.lists.all()
