import re


from codecs import open
from setuptools import setup, find_packages

version = ''
with open('lib/nelsnmp/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()

with open('HISTORY.rst', 'r', 'utf-8') as f:
    history = f.read()

long_description = readme + '\n\n' + history

config = {
    'name': 'nelsnmp',
    'package_dir': {'': 'lib'},
    'packages': find_packages('lib'),
    'version': version,
    'description': 'A wrapper module for pysnmp',
    'long_description': long_description,
    'author': 'Patrick Ogenstad',
    'author_email': 'patrick@ogenstad.com',
    'license': 'Apache',
    'url': 'https://networklore.com/nelsnmp/',
    'install_requires': ['pysnmp >= 4.3.1'],
    'classifiers': ['Development Status :: 4 - Beta',
                    'Intended Audience :: Developers',
                    'Intended Audience :: System Administrators']
}

setup(**config)
