#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='perfo_analysis',
      version='0.1',
      packages=find_packages(),
      package_data={'perfo_analysis': ['bin/*.*', 'static/*.*', 'templates/*.*']},
      exclude_package_data={'perfo_analysis': ['bin/*.pyc']},
      scripts=['perfo_analysis/bin/manage.py'])
