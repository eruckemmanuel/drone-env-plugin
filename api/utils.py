import logging

from api.models import EnvVariable

logger = logging.getLogger(__name__)


def add_env_variable(payload: dict) -> EnvVariable:
    """
    Add or update an environment variable
    """
    return EnvVariable.objects.update_or_create(
        name=payload.get('name'),
        defaults={
            'data': payload.get('data'),
            'mask': payload.get('mask', False)
        }
    )


def get_env_variables(filters: dict):
    """
    Get existing environment variables
    """
    env_vars = EnvVariable.objects.all()
    if filters:
        env_vars = env_vars.filter(**filters)

    return env_vars
