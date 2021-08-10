from django.db.models import fields
from rest_framework import serializers
from clients import models

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = '__all__'