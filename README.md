# crypto-price-scheduler

只是要讓 Google Sheet 透過 XML 的方式同步現在價格.

# 目錄
- [crypto-price-scheduler](#crypto-price-scheduler)
- [目錄](#目錄)
- [skills](#skills)
  - [Important Files](#important-files)
    - [How to create SECRET_KEY?](#how-to-create-secret_key)
    - [backend/app/config.py](#backendappconfigpy)

# skills

- Docker (Use Docker Services)
  - Docker-Compose
  - Redis
  - PostgreSQL ```not in v2(tag)```
  - Nginx
- Flask (backend)
- Flask jinja2 (backend's html)
- Flask-apscheduler (scheduler) ```not in v2(tag)```
- Celery ```start in v2(tag)```
- Uwsgi

## Important Files

### How to create SECRET_KEY?

```
==== generate SECRET_KEY ====
$ flask shell
>>> import os
>>> import base64
>>> a = os.urandom(24)
>>> base64.b64encode(a)
```


### backend/app/config.py 

```
class Config:
    SECRET_KEY = "PLEASE CREATE YOUR SECRET_KEY"

class developmentConfig(Config): 
    DEBUG = True
    REDIS_HOST = "localhost"
    REDIS_PORT = 6379
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/1'


class productionConfig(Config):
    DEBUG = False
    REDIS_HOST = "redis://redis"
    REDIS_PORT = 6379
    CELERY_BROKER_URL = 'redis://redis:6379/0'
    CELERY_RESULT_BACKEND = 'redis://redis:6379/1'


class testConfig(Config):
    TESTING = True
    REDIS_HOST = "localhost"
    REDIS_PORT = 6379
    CELERY_BROKER_URL = 'redis://localhost:6379/2'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/3'


config = {
    "development": developmentConfig,
    "production": productionConfig,
    "test": testConfig
}
```