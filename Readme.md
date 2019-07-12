# Python API Boilerplate - FastApi

FastApi Documentation [Read more](https://github.com/tiangolo/fastapi#performance)d

## Features

- Automatic documentation using swagger docs or Redoc
- Python types [Read More](https://fastapi.tiangolo.com/python-types/)
- Hot reaload, just keep coding and the server will restart itself!
- Remote Debugging

## Running the code

You should have docker and docker compose istalled. When starting the application will search for a `.env` file. If you don't have one you can copy the `development.env` as a base.

To start you development environment just run :

```sh
  docker-compose -f docker-compose.development.yml up
```

Or if you want to run the container in detached mode:

```sh
  docker-compose -f docker-compose.development.yml up -d
```

To stop it:

```sh
  docker-compose -f docker-compose.development.yml down
```
