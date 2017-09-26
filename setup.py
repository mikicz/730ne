from setuptools import setup

packages = [
    'Django<2',
    'psycopg2-binary',
    'social-auth-core==1.7.0',
    'social-auth-app-django==1.2.0',
]

if 'REDISCLOUD_URL' in os.environ \
   and 'REDISCLOUD_PORT' in os.environ and 'REDISCLOUD_PASSWORD' in os.environ:
    packages.append('django-redis-cache')
    packages.append('hiredis')

setup(name='730ne.cz', version='1.0',
      description='OpenShift Python-3.3 / Django-1.6 Community Cartridge based application',
      author='Miro Hroncok', author_email='miro@hroncok.cz',
      url='https://pypi.python.org/pypi',
      install_requires=packages,
      )
