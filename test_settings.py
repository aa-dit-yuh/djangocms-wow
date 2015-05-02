# -*- coding: utf-8 -*-
from distutils.version import LooseVersion
import sys
from tempfile import mkdtemp
import django

gettext = lambda s: s

HELPER_SETTINGS = {
    'INSTALLED_APPS': [
    ],
    'LANGUAGE_CODE': 'en',
    'LANGUAGES': (
        ('en', gettext('English')),
    ),
    'CMS_LANGUAGES': {
        1: [
            {
                'code': 'en',
                'name': gettext('English'),
                'public': True,
            },
        ],
        'default': {
            'hide_untranslated': False,
        },
    },
    'TEMPLATE_CONTEXT_PROCESSORS': {
        'sekizai.context_processors.sekizai'
    },
    'CMS_PERMISSION': True,
    'FILE_UPLOAD_TEMP_DIR': mkdtemp(),
    'SITE_ID': 1
}

if LooseVersion(django.get_version()) < LooseVersion('1.6'):
    HELPER_SETTINGS['INSTALLED_APPS'] += [
        'discover_runner'
    ]
    HELPER_SETTINGS['TEST_RUNNER'] = 'discover_runner.DiscoverRunner'


def run():
    import sys
    from djangocms_helper import runner
    runner.cms('djangocms_wow')

if __name__ == "__main__":
    run()

