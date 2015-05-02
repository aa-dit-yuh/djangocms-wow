djangocms-wow
=======================

.. image:: https://badge.fury.io/py/djangocms-wow.svg
    :target: http://badge.fury.io/py/djangocms-wow
.. image:: https://travis-ci.org/narayanaditya95/djangocms-wow.svg?branch=master
    :target: https://travis-ci.org/narayanaditya95/djangocms-wow
.. image:: https://coveralls.io/repos/narayanaditya95/djangocms-wow/badge.svg?branch=master
    :target: https://coveralls.io/r/narayanaditya95/djangocms-wow?branch=master
.. image:: https://landscape.io/github/narayanaditya95/djangocms-wow/master/landscape.svg?style=flat
    :target: https://landscape.io/github/narayanaditya95/djangocms-wow/master
    :alt: Code Health

Plugin for django-cms to include awesome animations from `WOW`_.js and `Animate`_.css

.. WOW: http://mynameismatthieu.com/WOW/
.. Animate: http://daneden.github.io/animate.css/


Installation
------------

This plugin requires `django CMS` 3.0 or higher to be properly installed.

* In your projects `virtualenv`, run ``pip install djangocms-text-ckeditor``.
* If using Django 1.6 add ``'djangocms_wow': 'djangocms_wow.south_migrations',``
  to ``SOUTH_MIGRATION_MODULES``  (or define ``SOUTH_MIGRATION_MODULES`` if it does not exists);
* Run ``manage.py migrate djangocms_wow``.


Usage
-----

Default content in Placeholder
******************************

If you use Django-CMS >= 3.0, you can use ``Animation`` in "default_plugins"
(see docs about the CMS_PLACEHOLDER_CONF setting in Django CMS 3.0).
