# Vaas
Here lies a bunch of tools we'll use for digital marketing automation.

### 1. Add credentials to config file

By default, credentials are saved in `config/.secrets`. Config file looks as follows:
```
[MonkeyLearn]
api_key=

[Shutterstock]
consumer_key=
consumer_secret=
```

### 2. Running tools locally

Run make file to start docker container and start FastApi server.
```
make
```

If image has not been created, run the following to build docker image and start server.
```
make buildup
```

### Docs
FastApi provides interactive api docs generated off of OpenAPI spec that can be views at http://0.0.0.0:8008/docs when 
running locally. 

Additional API Docs:
* [Recommendations API](app/docs/recommendations.md)
