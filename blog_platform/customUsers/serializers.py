import email
from rest_framework import serializers
from .models import CustomUser

class custUser_Serialization(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            role=validated_data.get('role', 'Member'),
            email=validated_data.get('email'),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user