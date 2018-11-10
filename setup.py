"""Requirements for the bot."""
from setuptools import setup

setup(
    name='replies_with_time',
    version='0.3',
    url='https://code.eons.io/sondr3/replieswithtime',
    author='Sondre Nilsen',
    author_email='nilsen.sondre@gmail.com',
    description='A bot that replies with the time!',
    extras_require={
        'dev': ['flake8', 'mypy', 'pylint', 'pycodestyle', 'pydocstyle'],
    },
    license='MIT'
)
