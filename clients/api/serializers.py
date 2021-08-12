from django.db.models import fields
from rest_framework import serializers
from clients import models

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = ['id','name', 'phone', 'address']
    address = AddressSerializer(many=False)

    def create(self,request, *args, **kwargs ):
        client_data = request

        new_address = models.Address.objects.create(**client_data['address'])
        new_address.save()
        client = models.Client.objects.create(name=client_data['name'], phone=client_data['phone'], address=new_address)
        client.save()
        return client
