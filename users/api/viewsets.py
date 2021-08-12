from users import models
from rest_framework import viewsets
from users.api import serializers
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User, Group


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer
    # permission_classes = [IsAuthenticated]