# drone-env-variable-plugin-api

[![Build Status](https://cicd.vehseh.com/api/badges/Vehseh/drone-env-plugin-api/status.svg)](https://cicd.vehseh.com/Vehseh/drone-env-plugin-api)

Plugin to store share environment variables across different pipelines


## Example usage in drone

```.yml
kind: pipeline
type: docker
name: default


steps:
  - name: env_server
    image: eruckemmanuel/drone-env-plugin-api
    detach: true
    commands:
      - python manage.py migrate
      - python manage.py runserver
```

You can then post environment variables to the server from any pipeline step

`POST http://env_server:8000/api/v1/env`
```.json
{
    "name": "DEPLOY_SERVER_IP",
    "data": "12.34.45.21"
}
```

And use it as environment plugin endpoint in any pipeline step

```.yml
kind: pipeline
type: docker
name: default


steps:
  - name: ping server
    image: python:3.9
    DRONE_ENV_PLUGIN_ENDPOINT: http://env_server:8000/api/v1/env
    commands:
      - ping $DEPLOY_SERVER_IP
      - python manage.py runserver
```

