DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'hathway_ecaf',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

import os

MEDIA_ROOT = os.path.join("C:\Users\Paktolususer\Github\hathway_ecaf", 'media')
MEDIA_URL = '/media/'