"""Requirements for the bot."""
from setuptools import setup, find_packages

setup(
    name='replies_with_time',
    version='0.2',
    url='https://code.eons.io/sondr3/replieswithtime',
    author='Sondre Nilsen',
    author_email='nilsen.sondre@gmail.com',
    description='A bot that replies with the time!',
    packages=find_packages(),
    install_requires=['tweepy', "arrow"],
    extras_require={
        'dev': ['flake8', 'mypy', 'pylint', 'pycodestyle', 'pydocstyle'],
    },
    license='MIT'
)
