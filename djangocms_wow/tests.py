# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.auth.models import User
from django.test import TestCase

from cms import api
from cms.models import CMSPlugin
from cms.test_utils.testcases import BaseCMSTestCase, URL_CMS_PLUGIN_ADD
from cms.utils import get_cms_setting

from .cms_plugins import AnimationPlugin, WOWAnimationPlugin


class AnimatePluginTestCase(TestCase, BaseCMSTestCase):
    su_username = 'user'
    su_password = 'pass'

    def setUp(self):
        self.template = get_cms_setting('TEMPLATES')[0][0]
        self.language = settings.LANGUAGES[0][0]
        self.page = api.create_page(
            'page',
            self.template,
            self.language,
            published=True
        )
        self.placeholder = self.page.placeholders.all()[0]
        self.superuser = self.create_superuser()

    def create_superuser(self):
        return User.objects.create_superuser(
            self.su_username,
            'email@example.com',
            self.su_password
        )

    def test_animation_not_infinite(self):
        self.client.login(username=self.su_username, password=self.su_password)

        plugin = api.add_plugin(
            self.placeholder,
            AnimationPlugin,
            self.language,
            animation_class='shake',
            infinite=False,
        )
        self.page.publish(self.language)
        url = self.page.get_absolute_url()
        response = self.client.get(url)

        self.assertContains(response, 'animate.css')
        self.assertContains(response, 'shake')
        self.assertNotContains(response, 'infinite')
        self.assertEqual(plugin.__str__(), 'Animate shake')
        self.page.delete()


    def test_animation_infinite(self):
        self.client.login(username=self.su_username, password=self.su_password)

        plugin = api.add_plugin(
            self.placeholder,
            AnimationPlugin,
            self.language,
            animation_class='wobble',
            infinite=True,
        )
        self.page.publish(self.language)
        url = self.page.get_absolute_url()
        response = self.client.get(url)

        self.assertContains(response, 'animate')
        self.assertContains(response, 'wobble')
        self.assertContains(response, 'infinite')


    def test_wow_animation_no_additional_arguments(self):
        self.client.login(username=self.su_username, password=self.su_password)

        plugin = api.add_plugin(
            self.placeholder,
            WOWAnimationPlugin,
            self.language,
            animation_class='flash',
        )
        self.page.publish(self.language)
        url = self.page.get_absolute_url()
        response = self.client.get(url)

        self.assertContains(response, 'wow')
        self.assertNotContains(response, 'duration')
        self.assertNotContains(response, 'delay')
        self.assertNotContains(response, 'offset')
        self.assertNotContains(response, 'iteration')


    def test_wow_animation_all_arguments(self):
        self.client.login(username=self.su_username, password=self.su_password)

        plugin = api.add_plugin(
            self.placeholder,
            WOWAnimationPlugin,
            self.language,
            animation_class='hinge',
            duration=1,
            delay=2,
            offset=3,
            iteration=4,
        )
        self.page.publish(self.language)
        url = self.page.get_absolute_url()
        response = self.client.get(url)

        self.assertContains(response, 'wow.js')
        self.assertContains(response, 'hinge')
        self.assertContains(response, 'data-wow-duration="1s"')
        self.assertContains(response, 'data-wow-delay="2s"')
        self.assertContains(response, 'data-wow-offset="3"')
        self.assertContains(response, 'data-wow-iteration="4"')
