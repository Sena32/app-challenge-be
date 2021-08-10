from clients import models
from rest_framework import viewsets
from clients.api import serializers
from rest_framework.permissions import IsAuthenticated

class ClientViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.ClientSerializer
    queryset = models.Client.objects.all()