#!/usr/bin/env python

#from distutils.core import setup
from setuptools import setup, find_packages

setup(name='nep_fitting',
      version='1.9',
      description='Nested-loop Ensemble PSF fitting',
      author='Andrew Barentine, Michael Graff, David Baddeley',
      author_email='andrew.barentine@yale.edu',
      packages=find_packages(),
      package_data={
            # include all svg and html files, otherwise conda will miss them
            '': ['*.svg', '*.html'],
      }
     )
