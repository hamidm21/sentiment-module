from setuptools import setup, find_packages

__version__= 'dev'

setup(
    name='sentiment-module',
    version=__version__,

    url='https://github.com/hamidm21/sentiment-module.git',
    author='Hamid Moradi',
    author_email='hordimad21@gmail.com',

    packages = find_packages()
)