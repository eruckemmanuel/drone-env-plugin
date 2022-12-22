from rest_framework import serializers

from api.models import EnvVariable


class EnvVariableSerializer(serializers.ModelSerializer):

    class Meta:
        model = EnvVariable
        fields = ("name", "data", "mask",)


def get_serialized_env_variable(env_var, many=False):
    return EnvVariableSerializer(env_var, many=many).data
