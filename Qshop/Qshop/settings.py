"""
Django settings for Qshop project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'aucsr841v)rr*fz126=zx#vbsd9q4p*&m7hp-v1p4#qt#twkv8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Buyer',
    'Seller',
    'djcelery'
]

MIDDLEWARE = [
    # 'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'Qshop.middleware01.MiddleWareTest',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
]

ROOT_URLCONF = 'Qshop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Qshop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'qshop',
        'USER':'root',
        'PASSWORD':'111111',
        'HOST':'127.0.0.1',
        'PORT':'3306'
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

# USE_TZ = True
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR,"static"),
)
# STATIC_ROOT = os.path.join(BASE_DIR,"static")

## 媒体文件配置
# MEDIA
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,"static")



##  支付宝支付 demo
alipay_public_key_string="""-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAh5AE4ca3NYqqXy9FLqg2hJgi6SmJrIe4nE+dPmDn6BWW8N+JltCI5A9TMEwMiQyENaCO2XpaZlh5UVi5pJE45Sa2pelmgeN/7M73zLn5UZwPjIwdYpFU+P16yD5IyhQusmB4cKIReT0jkcj0IBCp7Iyb5QugVmgxqgA8svHRKQg3p/aE1e1/HiLxReIFvHg9CUuFUwmJ7dLQ1k4sxgoxzKA/pj99FThptCFu+wA0GUPT3I/T42PoVmf/UZ/fHn7qdLc9TxanvU8sSU7UtXms5m56qqh6H8YgUPlGDVetWU/HR+VAAEJc5RMcXGEHqeqp7NFe9zZhxOr61r4P0HzUrwIDAQAB
-----END PUBLIC KEY-----"""
app_private_key_string="""-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAh5AE4ca3NYqqXy9FLqg2hJgi6SmJrIe4nE+dPmDn6BWW8N+JltCI5A9TMEwMiQyENaCO2XpaZlh5UVi5pJE45Sa2pelmgeN/7M73zLn5UZwPjIwdYpFU+P16yD5IyhQusmB4cKIReT0jkcj0IBCp7Iyb5QugVmgxqgA8svHRKQg3p/aE1e1/HiLxReIFvHg9CUuFUwmJ7dLQ1k4sxgoxzKA/pj99FThptCFu+wA0GUPT3I/T42PoVmf/UZ/fHn7qdLc9TxanvU8sSU7UtXms5m56qqh6H8YgUPlGDVetWU/HR+VAAEJc5RMcXGEHqeqp7NFe9zZhxOr61r4P0HzUrwIDAQABAoIBADagcWcttVwtAZSTrtQrUrTBvaepZmIQ2vKaHmopkKn0MTvlSENuywrjpgkbTB3Z3ljh106JwG3njxOZpk1Le9rTa9yVngoPS9h4WmC0PGSHd7iSKbEzkUM4mcahWqGb2mlk+IOiu1nYqkGv8bgOHvtEefmlYroPCJxRtiQBz+AxY7h3nrG4okeV19SAYi60wA9/z49PfoldXVfDos9pMuLTDQmk5xR424Y00Qu2fObAdiwMv4Muhb1hDlmPw7a9ErsSGp6aIUD0dB7EieYuwynUUNaKE/J+V4L8ApNvhvpQK5YDCTA4guRo6T75fsjSekd5SORrtF1/totLxHaULyECgYEA+qMFfOpXOcoA/aGO6z3GZOZlKeZG03QnEpIQ8DAfkyqOWSmu0AyFgZKVvCDqMGPNUMZoGxbyGw83A1aTFnwqdk5tSmnNBxQiMlfOjUNMrPdRAl+i8lV5ymjPToWi/os2mX0gks8YPsmNtPgMIEZ4sJ3eLaojTEjYcKNlPN5IvJ8CgYEAinagIr+/wns+0MBE9qgT3m9OeekF7h5Hqy2xI2QtnpCkLdg4JXblpLh9/UZUeXmP8HSIkNoI41n9RW7qzgTWx83zvIHhqheKeJRKROss5kJtciOUMnOL+XSK43DFAz0KeXz1/HvWdc6OKRx5mz3cPplkUGkwqU+iynW074AS3fECgYEA3Gyk9fAOmFdMucLtM3wX0END8y5/WZZMiquFVAeurTn/CPF8uaJZg9QL9fEopTgQqJplknWCpUOjST9JirvWiEd/HLOhyjjtvkK0+E2Y0IGNcD31y5Ra0SWONGuZJq3+bcy66gJSO139T4va9kOj/whIDvcTphJmr+Eztu1zINcCgYBp7DuuuY9hoNS57wwSwRuKAw4+tqOBuIpNCkRDdcRsU+w04f55so4Ux8oh8iZ3UyZo5Uz/urwn6FSXRDW96ve/m+8EWzud2ipk+dQjCuGrOE/vjAY33irLZ3tEaKVeR9j2fUDUqIu0TZJ1IsJonxcYkFGsLfw62aAIT6ldulU0kQKBgQD2ndjwswgtl7vVetmTqmbDEHR3F43Xz0AtEw6CJyfU9Ai3Sy5rv99a/Qyv9DnW/GlcDp7/fI9C8dnzAbqcRPjHaQrXwpZbQiqTr1gmGypBqV4OuU6LBA5xcgY02vDKXZ7nQC4bCeFjDtIfEjvUXE5Xlc1ILdT1Ghh9hIBAhXjcOQ==
-----END RSA PRIVATE KEY-----"""

# 1、 导包
from alipay import AliPay

# 2、 创建一个实例对象
alipay =AliPay(
    appid="2016101300673550",
    app_notify_url=None,
    app_private_key_string=app_private_key_string,
    alipay_public_key_string=alipay_public_key_string,
    sign_type="RSA2",
    debug=False
)

# ## celery 配置
import djcelery  ## 导包
djcelery.setup_loader()   ## 模块加载
BROKER_URL = "redis://127.0.0.1:6379/1"    ### 指定broker 的存储位置 ，消息中间件（redis）   中间人
CELERY_IMPORTS = ('CeleryTask.tasks')     ## 指定任务文件
## 时区
CELERY_TIMEZONE = 'Asia/Shanghai'
## celery 调度器  ## 固定写法
CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"

from celery.schedules import timedelta,crontab
CELERYBEAT_SCHEDULE = {
    u"测试01":{
        "task":"CeleryTask.tasks.Test",         ### 定时任务要是执行的任务
        # "schedule":timedelta(seconds=2)        ## 每两秒执行一次
        # "schedule":crontab(hour=2)        ## 每两小时执行一次
        "schedule":crontab(minute=2)        ## 每两分钟时执行一次
    }
}

## 缓存
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION':[
            "127.0.0.1:11211"        #### 使用本地的memcache 缓存
        ]
    }
}

