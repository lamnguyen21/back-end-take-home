This project uses Python 3 and Flask framework (https://flask.palletsprojects.com/en/1.1.x/)

## Installation ##
Python 3
Python Virtual Env
Run `pip install -r requirements.txt`

## Unit Tests ##
Run `coverage run -m pytest`

## Start the backend service ##
### Prepare app configuration ###
At startup, the service tries to load configurations from a config file. The path to this config file should be defined by an environment variable named `APP_CONFIG`. The config file should define absolute paths to `routes.csv` and `airports.csv`. For example:
```
AIRPORTS="<<path prefix>>/airports.csv"
ROUTES="<<path prefix>>/routes.csv"
```
### Run the service ###
There are two ways:
 - Run `flask run`. The endpoint is accessible at 'http://localhost:5000/routes/<start>/to<end>"
 - Run `uwsgi --socket 0.0.0.0:8000 --protocol=http --module wsgi:app`. The endpoint is accessible at `http://localhost:8000/routes/<start>/to/<end>`

For example: 'http://localhost:5000/routes/YVR/to/LAX'

## Hosted version ##

The same service is hosted on DigitalOcean and is available at `http://guestlogix.istockstaker.ml/routes/YVR/to/LAX`
