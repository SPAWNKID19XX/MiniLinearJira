from rest_framework import serializers
from config.settings import AUTH_USER_MODEL


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = AUTH_USER_MODEL
    fields = ["first_name", "last_name", "email", "password"]
    extra_kwargs= {
      "password":{
        "write_only": True
      }
    }

  def create(self, validated_data):
    return AUTH_USER_MODEL.objects.create_user(**validated_data)

  def update(self, instance, validated_data):

    pass_date = validated_data.get("password", None)

    instance = super().update(instance, validated_data)

    if pass_date:
      instance.set_password(pass_date)
      instance.save()

    return instance
      