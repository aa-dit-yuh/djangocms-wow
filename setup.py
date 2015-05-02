#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
from djangocms_wow import __version__


INSTALL_REQUIRES = [
    'django-cms>=3.0',
]

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Communications',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Message Boards',
    "Programming Language :: Python :: 2.6",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
]

setup(
    name='djangocms-wow',
    version=__version__,
    description='Plugin for django-cms to include awesome animations from WOW.js and Animate.css',
    author='Aditya Narayan',
    author_email='narayanaditya95@gmail.com',
    url='https://github.com/narayanaditya95/djangocms-wow',
    packages=['djangocms_wow', 'djangocms_wow.migrations', 'djangocms_wow.south_migrations'],
    install_requires=INSTALL_REQUIRES,
    license='LICENSE.txt',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    long_description=open('README.rst').read(),
    include_package_data=True,
    zip_safe=False,
    test_suite='test_settings.run',
)
