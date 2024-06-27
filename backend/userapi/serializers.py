from rest_framework import serializers
from .models import *
from .validators import *


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    phone = serializers.CharField(validators=[validate_phone])
    pincode = serializers.CharField(validators=[validate_pincode])
    class Meta:
        model=User
        fields='__all__'
    def create(self, validated_data):
        user=User.objects.create(
            full_name=validated_data['full_name'],
            email=validated_data['email'],
            phone=validated_data['phone'],
            address=validated_data['address'],
            city=validated_data['city'],
            state=validated_data['state'],
            country=validated_data['country'],
            pincode=validated_data['pincode'],
            
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
