import logging

from rest_framework.views import APIView
from rest_framework.response import Response

from api.utils import (add_env_variable, get_env_variables)
from api.serializers import get_serialized_env_variable

logger = logging.getLogger(__name__)


class EnvAPIView(APIView):

    def post(self, request):
        """
        Handle POST request to add env variable
        """
        env_var, created = add_env_variable(request.data)
        return Response(get_serialized_env_variable(env_var))

    def get(self, request):
        env_vars = get_env_variables(request.query_params)
        return Response(get_serialized_env_variable(env_vars, many=True))

