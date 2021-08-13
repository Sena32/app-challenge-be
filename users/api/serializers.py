from django.contrib.auth.models import User
from rest_framework import serializers
from django.apps import apps
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
    
    # def create(self, request, **extra_fields):
    #     user_data = request
    #     # print(user_data)
    #     # return
    #     if not user_data['username']:
    #         raise ValueError('The given username must be set')
    #     email = self.normalize_email(user_data['email'])
    #     # Lookup the real model class from the global app registry so this
    #     # manager method can be used in migrations. This is fine because
    #     # managers are by definition working on the real model.
    #     GlobalUserModel = apps.get_model(self.model._meta.app_label, self.model._meta.object_name)
    #     username = GlobalUserModel.normalize_username(user_data['username'])
    #     user = self.model(username=username, email=email, **extra_fields)
    #     user.password = make_password(user_data['password'])
    #     user.save(using=self._db)
    #     return user