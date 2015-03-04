from nelsnmp import __version__
from nelsnmp import __author__
from setuptools import setup

config = {
    'name': 'nelsnmp',
    'packages': ['nelsnmp'],
    'version': __version__,
    'description': 'A wrapper module for pysnmp',
    'author': __author__,
    'author_email': 'patrick@ogenstad.com',
    'license': 'Apache',
    'url': 'http://networklore.com/nelsnmp/',
    'install_requires': ['pysnmp >= 4.2.5'],
    'classifiers': ['Development Status :: 4 - Beta',
                    'Intended Audience :: Developers',
                    'Intended Audience :: System Administrators']
} 

setup(**config)

