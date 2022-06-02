# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Real-Time Twitch Messaging Analytics',
    version='0.1.0',
    description='Placeholder',
    long_description=readme,
    author='David Shipman',
    author_email='davidshipmanchs2020@gmail.com',
    url='https://github.com/DavidJS01/Real-Time-Twitch-Messaging-Analytics',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)