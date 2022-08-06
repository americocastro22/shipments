# shipments
API for Shipments.

## Install and run

### Development

#### Install
```bash
git clone https://github.com/americocastro22/shipments shipments
```
```bash
cd shipments
```
```bash
Then Create a virtual environment and activate it, after that:
pip install -e .
```

#### Enviroment Variables
```bash
Copy the file .env.example to .env and fill the information.
```


| Name                      | Default value                    | Description                                                                                                                                 |
|---------------------------|----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| PROJECT_BASE_DIR          | `''` (current working directory) | Folder containing the project runtime files: `.env`, databases, media and collected statics.                                                |
| LOAD_DOTENV               | `True`                           | Try to load environment variables from `$PROJECT_BASE_DIR/.env` file.                                                                       |
| SECRET_KEY                |                                  | Django [`SECRET_KEY`](https://docs.djangoproject.com/en/3.2/ref/settings/#std:setting-SECRET_KEY) setting.                                  |
| DEBUG                     | `False`                          | Django [`DEBUG`](https://docs.djangoproject.com/en/3.2/ref/settings/#debug) setting.                                                        |
| ALLOWED_HOSTS             | `[]`                             | Django [`ALLOWED_HOSTS`](https://docs.djangoproject.com/en/3.2/ref/settings/#allowed-hosts) setting.                                        |
| INTERNAL_IPS              | `[]`                             | Django [`INTERNAL_IPS`](https://docs.djangoproject.com/en/3.2/ref/settings/#internal-ips) setting. Also used to activate the debug toolbar. |

#### Prepare
```bash
python manage.py migrate
```

#### Run
```bash
python manage.py runserver
```