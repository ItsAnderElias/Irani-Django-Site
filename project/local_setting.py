# type: ignore
# flake8: noqa

# Comando:
# python -c "import string as s;from secrets import SystemRandom as SR;print(''.join(SR().choices(s.ascii_letters + s.digits + s.punctuation, k=64)));"
SECRET_KEY = 'gfXDk:65Db@y<aSw?pHnUwu,z^^w4YVE||$nJ&Wt,-J%,bV;O3!~R`%KdGf0b&a?'

# DEBUG DEVE SER False em produção
DEBUG = False

# Seu domínio ou IP devem vir aqui
ALLOWED_HOSTS = [
    '192.168.0.195',
]  # Troque * para seu domínio ou IP

# Config para postgresql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'projeto_irani',
        'USER': 'usuario_irani',
        'PASSWORD': 'senha_irani',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}