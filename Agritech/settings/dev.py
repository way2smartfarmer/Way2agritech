from .common import *


DEBUG = True
SECRET_KEY = 'django-insecure-6w%a23u&h(@htqyq0h*e7+!=1mh%!!m_8zkoc8efo1bzst$#0_'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'agritech',
        'HOST': '127.0.0.1',
        'PORT': '3006',
        'USER': 'root',
        'PASSWORD': 'Mysql@way2agri'
    }
}
