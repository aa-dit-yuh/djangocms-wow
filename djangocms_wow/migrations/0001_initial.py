# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animation',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('animation_class', models.CharField(default=b'bounce', max_length=25, choices=[(b'bounce', 'Bounce'), (b'flash', 'Flash'), (b'pulse', 'Pulse'), (b'rubberBand', 'Rubber Band'), (b'shake', 'Shake'), (b'swing', 'Swing'), (b'tada', 'Ta-Da'), (b'wobble', 'Wobble'), (b'bounceIn', 'Bounce In'), (b'bounceInDown', 'Bounce In Down'), (b'bounceInLeft', 'Bounce In Left'), (b'bounceInRight', 'Bounce In Right'), (b'bounceInUp', 'Bounce In Up'), (b'bounceOut', 'Bounce Out'), (b'bounceOutDown', 'Bounce Out Down'), (b'bounceOutLeft', 'Bounce Out Left'), (b'bounceOutRight', 'Bounce Out Right'), (b'bounceOutUp', 'Bounce Out Up'), (b'fadeIn', 'Fade In'), (b'fadeInDown', 'Fade In Down'), (b'fadeInDownBig', 'Fade In Down Big'), (b'fadeInLeft', 'Fade In Left'), (b'fadeInLeftBig', 'Fade In Left Big'), (b'fadeInRight', 'Fade In Right'), (b'fadeInRightBig', 'Fade In Right Big'), (b'fadeInUp', 'Fade In Up'), (b'fadeInUpBig', 'Fade In Up Big'), (b'fadeOut', 'Fade Out'), (b'fadeOutDown', 'Fade Out Down'), (b'fadeOutDownBig', 'Fade Out Down Big'), (b'fadeOutLeft', 'Fade Out Left'), (b'fadeOutLeftBig', 'Fade Out Left Big'), (b'fadeOutRight', 'Fade Out Right'), (b'fadeOutRightBig', 'Fade Out Right Big'), (b'fadeOutUp', 'Fade Out Up'), (b'fadeOutUpBig', 'Fade Out Up Big'), (b'flipInX', 'Flip In X'), (b'flipInY', 'Flip In Y'), (b'flipOutX', 'Flip Out X'), (b'flipOutY', 'Flip Out Y'), (b'lightSpeedIn', 'Light Speed In'), (b'lightSpeedOut', 'Light Speed Out'), (b'rotateIn', 'Rotate In'), (b'rotateInDownLeft', 'Rotate In Down Left'), (b'rotateInDownRight', 'Rotate In Down Right'), (b'rotateInUpLeft', 'Rotate In Up Left'), (b'rotateInUpRight', 'Rotate In Up Right'), (b'rotateOut', 'Rotate Out'), (b'rotateOutDownLeft', 'Rotate Out Down Left'), (b'rotateOutDownRight', 'Rotate Out Down Right'), (b'rotateOutUpLeft', 'Rotate Out Up Left'), (b'rotateOutUpRight', 'Rotate Out Up Right'), (b'hinge', 'Hinge'), (b'rollIn', 'Roll In'), (b'rollOut', 'Roll Out'), (b'zoomIn', 'Zoom In'), (b'zoomInDown', 'Zoom Out'), (b'zoomInLeft', 'Zoom In Left'), (b'zoomInRight', 'Zoom In Right'), (b'zoomInUp', 'Zoom In Up'), (b'zoomOut', 'Zoom Out'), (b'zoomOutDown', 'Zoom Out Down'), (b'zoomOutLeft', 'Zoom Out Left'), (b'zoomOutRight', 'Zoom Out Right'), (b'zoomOutUp', 'Zoom Out Up'), (b'slideInDown', 'Slide In Down'), (b'slideInLeft', 'Slide In Left'), (b'slideInRight', 'Slide In Right'), (b'slideInUp', 'Slide In Up'), (b'slideOutDown', 'Slide Out Down'), (b'slideOutLeft', 'Slide Out Left'), (b'slideOutRight', 'Slide Out Right'), (b'slideOutUp', 'Slide Out Up')])),
                ('infinite', models.NullBooleanField(help_text='Infinite Loop')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='WOWAnimation',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('animation_class', models.CharField(default=b'bounce', max_length=25, choices=[(b'bounce', 'Bounce'), (b'flash', 'Flash'), (b'pulse', 'Pulse'), (b'rubberBand', 'Rubber Band'), (b'shake', 'Shake'), (b'swing', 'Swing'), (b'tada', 'Ta-Da'), (b'wobble', 'Wobble'), (b'bounceIn', 'Bounce In'), (b'bounceInDown', 'Bounce In Down'), (b'bounceInLeft', 'Bounce In Left'), (b'bounceInRight', 'Bounce In Right'), (b'bounceInUp', 'Bounce In Up'), (b'bounceOut', 'Bounce Out'), (b'bounceOutDown', 'Bounce Out Down'), (b'bounceOutLeft', 'Bounce Out Left'), (b'bounceOutRight', 'Bounce Out Right'), (b'bounceOutUp', 'Bounce Out Up'), (b'fadeIn', 'Fade In'), (b'fadeInDown', 'Fade In Down'), (b'fadeInDownBig', 'Fade In Down Big'), (b'fadeInLeft', 'Fade In Left'), (b'fadeInLeftBig', 'Fade In Left Big'), (b'fadeInRight', 'Fade In Right'), (b'fadeInRightBig', 'Fade In Right Big'), (b'fadeInUp', 'Fade In Up'), (b'fadeInUpBig', 'Fade In Up Big'), (b'fadeOut', 'Fade Out'), (b'fadeOutDown', 'Fade Out Down'), (b'fadeOutDownBig', 'Fade Out Down Big'), (b'fadeOutLeft', 'Fade Out Left'), (b'fadeOutLeftBig', 'Fade Out Left Big'), (b'fadeOutRight', 'Fade Out Right'), (b'fadeOutRightBig', 'Fade Out Right Big'), (b'fadeOutUp', 'Fade Out Up'), (b'fadeOutUpBig', 'Fade Out Up Big'), (b'flipInX', 'Flip In X'), (b'flipInY', 'Flip In Y'), (b'flipOutX', 'Flip Out X'), (b'flipOutY', 'Flip Out Y'), (b'lightSpeedIn', 'Light Speed In'), (b'lightSpeedOut', 'Light Speed Out'), (b'rotateIn', 'Rotate In'), (b'rotateInDownLeft', 'Rotate In Down Left'), (b'rotateInDownRight', 'Rotate In Down Right'), (b'rotateInUpLeft', 'Rotate In Up Left'), (b'rotateInUpRight', 'Rotate In Up Right'), (b'rotateOut', 'Rotate Out'), (b'rotateOutDownLeft', 'Rotate Out Down Left'), (b'rotateOutDownRight', 'Rotate Out Down Right'), (b'rotateOutUpLeft', 'Rotate Out Up Left'), (b'rotateOutUpRight', 'Rotate Out Up Right'), (b'hinge', 'Hinge'), (b'rollIn', 'Roll In'), (b'rollOut', 'Roll Out'), (b'zoomIn', 'Zoom In'), (b'zoomInDown', 'Zoom Out'), (b'zoomInLeft', 'Zoom In Left'), (b'zoomInRight', 'Zoom In Right'), (b'zoomInUp', 'Zoom In Up'), (b'zoomOut', 'Zoom Out'), (b'zoomOutDown', 'Zoom Out Down'), (b'zoomOutLeft', 'Zoom Out Left'), (b'zoomOutRight', 'Zoom Out Right'), (b'zoomOutUp', 'Zoom Out Up'), (b'slideInDown', 'Slide In Down'), (b'slideInLeft', 'Slide In Left'), (b'slideInRight', 'Slide In Right'), (b'slideInUp', 'Slide In Up'), (b'slideOutDown', 'Slide Out Down'), (b'slideOutLeft', 'Slide Out Left'), (b'slideOutRight', 'Slide Out Right'), (b'slideOutUp', 'Slide Out Up')])),
                ('duration', models.PositiveSmallIntegerField(help_text='Change the animation duration', null=True, blank=True)),
                ('delay', models.PositiveSmallIntegerField(help_text='Delay before the animation starts', null=True, blank=True)),
                ('offset', models.PositiveSmallIntegerField(help_text='Distance to start the animation (related to the browser bottom)', null=True, blank=True)),
                ('iteration', models.PositiveSmallIntegerField(help_text='Number of times the animation is repeated', null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
