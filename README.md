# WEB APP

## Configuration
If additional configuration is needed to override the default configuration in default_config.json, then
the following environment variable must be set:

```
export SETTINGS=/full/path/to/config.json
```
This config.json contains the settings that will override default_config.json. If SETTINGS is not set, the application will only use default_config.json.

If running the app flask the "flask run" command, then the following environment variable must be set.

```
export FLASK_APP=app/app.py
```
This application can then be launched from within the root directory.

If the application is to be run in development mode (reloader and debug):

```
export FLASK_ENV=development
```

## Usage

After configuration, the flask app can be launched with:

```
flask run
```

If using gunicorn, it is also possible to launch the app using the following command from the root directory:

```
gunicorn -w 4 "app.app:create_app()"
```





