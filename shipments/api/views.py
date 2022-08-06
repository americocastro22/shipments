from django.http import HttpRequest
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin, ListModelMixin, RetrieveModelMixin,
                                   UpdateModelMixin)
from rest_framework.parsers import JSONParser

from .serializers import ShipmentSerializer
from .models import Shipment


class ShipmentList(ListModelMixin,
                   CreateModelMixin,
                   GenericAPIView):
    """
    View for list and create shipments.
    """
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer
    parser_classes = [JSONParser]

    def get(self, request: HttpRequest, *args, **kwargs):
        """
        Retrieves a list of shipments.
        """
        return self.list(request, *args, **kwargs)

    def post(self, request: HttpRequest, *args, **kwargs):
        """
        Create a shipment instance.
        """
        return self.create(request, *args, **kwargs)


class ShipmentDetail(RetrieveModelMixin,
                     UpdateModelMixin,
                     DestroyModelMixin,
                     GenericAPIView):
    """
    View for retrieving, updating or deleting a shipment instance.
    """
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer
    parser_classes = [JSONParser]

    def get(self, request: HttpRequest, *args, **kwargs):
        """
        Retrieve a shipment instance.
        """
        return self.retrieve(request, *args, **kwargs)

    def put(self, request: HttpRequest, *args, **kwargs):
        """
        Update a shipment instance.
        """
        return self.update(request, *args, **kwargs)

    def delete(self, request: HttpRequest, *args, **kwargs):
        """
        Delete a shipment instance.
        """
        return self.destroy(request, *args, **kwargs)
