from setuptools import setup, find_packages

setup(
    name='sentimod',
    version='dev',

    url='https://github.com/hamidm21/sentiment-module.git',
    author='Hamid Moradi',
    author_email='hordimad21@gmail.com',

    packages = find_packages(
        where='src'
    )
)