# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-bk-hhwd_)-!yq(q&sfml7u9_j#i-2-+*_j9fqzx_t=2l3aj#om'

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'music_library_database',
        'USER': 'root',
        'PASSWORD': 'Esther1991',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}
