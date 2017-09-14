#!/usr/bin/env python

#from distutils.core import setup
from setuptools import setup, find_packages

setup(name='nep_fitting',
      version='1.0',
      description='Nested Ensemble Resolution Estimation',
      author='Andrew Barentine, Michael Graff, David Baddeley',
      author_email='gward@python.net',
      #url='https://www.python.org/sigs/distutils-sig/',
      packages=find_packages(),
     )