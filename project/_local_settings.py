# type: ignore
# flake8: noqa

# Comando:
# python -c "import string as s;from secrets import SystemRandom as SR;print(''.join(SR().choices(s.ascii_letters + s.digits + s.punctuation, k=64)));"
SECRET_KEY = 'CHANGEME'

# DEBUG DEVE SER False em produção
DEBUG = False

# Seu domínio ou IP devem vir aqui
ALLOWED_HOSTS = [
    'CHANGEME',
]  # Troque * para seu domínio ou IP

# Config para postgresql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'CHANGEME',
        'USER': 'CHANGEME',
        'PASSWORD': 'CHANGEME',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}