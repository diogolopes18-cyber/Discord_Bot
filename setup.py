#!/usr/bin/env python3

from setuptools import setup

setup(
    name='bot',
    author='Diogo Lopes & Ivan Pinto & Luís Araújo',
    version='1.0.0',
    packages=['bot'],
    install_requires=['python-dotenv==0.15.0',
                      'asyncio==3.4.3',
                      'discord==1.7.3',
                      'requests==2.22.0',
                      'wikipedia==1.4.0',
                      'Flask==2.0.2']
)
