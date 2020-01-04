from django_filters import rest_framework as filters
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .filters import LinkFilter
from .models import Link, List
from .serializers import LinkSerializer, ListSerializer


# thanks to https://www.revsys.com/tidbits/keeping-django-model-objects-ordered/
class LinkViewSet(viewsets.ModelViewSet):
    serializer_class = LinkSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = LinkFilter

    def get_queryset(self):
        return self.request.user.links.all()

    @action(methods=["POST"], detail=True)
    def move(self, request, pk):
        obj = self.get_object()
        new_order = request.data.get("order", None)

        # Verify we received an order
        if new_order is None:
            return Response(
                data={"error": "No order given"}, status=status.HTTP_400_BAD_REQUEST
            )

        if new_order < 1:
            return Response(
                data={"error": "Order cannot be zero or below"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        Link.objects.move(obj, new_order)

        return Response({"success": True, "order": new_order})


class ListViewSet(viewsets.ModelViewSet):
    serializer_class = ListSerializer

    def get_queryset(self):
        return self.request.user.lists.all()

    @action(methods=["POST"], detail=True)
    def move(self, request, pk):
        obj = self.get_object()
        new_order = request.data.get("order", None)

        # Verify we received an order
        if new_order is None:
            return Response(
                data={"error": "No order given"}, status=status.HTTP_400_BAD_REQUEST
            )

        if new_order < 1:
            return Response(
                data={"error": "Order cannot be zero or below"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        List.objects.move(obj, new_order)

        return Response({"success": True, "order": new_order})
