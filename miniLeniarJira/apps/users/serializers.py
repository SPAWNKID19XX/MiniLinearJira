from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ["first_name", "last_name", "email", "password"]
    extra_kwargs= {
      "password":{
        "write_only": True
      }
    }

  def create(self, validated_data):
    return User.objects.create_user(**validated_data)

  def update(self, instance, validated_data):

    pass_date = validated_data.get("password", None)

    instance = super().update(instance, validated_data)

    if pass_date:
      instance.set_password(pass_date)
      instance.save()

    return instance
      