from rest_framework import viewsets

from .serializers import LinkSerializer, ListSerializer


class LinkViewSet(viewsets.ModelViewSet):
    serializer_class = LinkSerializer

    def get_queryset(self):
        return self.request.user.links.all()


class ListViewSet(viewsets.ModelViewSet):
    serializer_class = ListSerializer

    def get_queryset(self):
        return self.request.user.lists.all()
