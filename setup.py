from setuptools import setup, find_packages

__version__= 'dev'
packages = find_packages()

setup(
    name='sentiment-module',
    version=__version__,

    url='https://github.com/MichaelKim0407/tutorial-pip-package',
    author='Michael Kim',
    author_email='mkim0407@gmail.com',

    py_modules=['my_pip_package'],
)