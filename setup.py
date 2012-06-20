#!/usr/bin/env python
from setuptools import setup, find_packages


setup(name='narcissus',
      version='0.1',
      url='https://github.com/codeinthehole/narcissus',
      author="David Winterbottom",
      author_email="david.winterbottom@tangentlabs.co.uk",
      description="Vanity metrics for your project",
      long_description=open('README.rst').read(),
      packages=find_packages(),
      scripts=['bin/narcissus'],
      dependencies=['beautifulsoup4==4.1.0',
                    'pygithub3==0.4',
                    'envoy==0.0.2']
     )
