from rest_framework import serializers
# from Regi_api.models import Adduser
# from rest_framework.validators import UniqueValidator
# from django.contrib.auth.models import User
from .models import *

class SnippetSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255, write_only=True)
    email = serializers.CharField(max_length=255, write_only=True)
    password = serializers.CharField(max_length=255, write_only=True)
    id = serializers.CharField(read_only=True)

    def validate(self, data):

        username = data.get("username", None)
        email = data.get("email", None)
        password = data.get("password", None)
        # request = self.context.get("request")
        # user = request.user
        if Adduser.objects.filter(username=username).exists():
            raise serializers.ValidationError('User already exist')
        
        username = username.capitalize()
        adduser = Adduser.objects.create(username=username, email=email, password=password)
        adduser.save()
        return {'user': username}




# class SnippetSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'password', 'email')
#         write_only_fields = ('password',)
#         read_only_fields = ('id',)

#     def create(self, validated_data):
#         user = User.objects.create(
#             username=validated_data['username'],
#             email=validated_data['email'],
#         )

#         user.set_password(validated_data['password'])
#         user.save()

#         return user