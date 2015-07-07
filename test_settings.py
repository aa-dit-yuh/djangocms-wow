# -*- coding: utf-8 -*-
from distutils.version import LooseVersion
import sys
from tempfile import mkdtemp
import django

gettext = lambda s: s

HELPER_SETTINGS = {
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
    },
    'CMS_PERMISSION': True,
    'FILE_UPLOAD_TEMP_DIR': mkdtemp(),
    'SITE_ID': 1
}

def run():
    import sys
    from djangocms_helper import runner
    runner.cms('djangocms_wow')

if __name__ == "__main__":
    run()

