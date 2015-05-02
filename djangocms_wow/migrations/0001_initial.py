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
                ('cmsplugin_ptr', models.OneToOneField(serialize=False, primary_key=True, parent_link=True, auto_created=True, to='cms.CMSPlugin')),
                ('animation_class', models.CharField(default='bounce', choices=[('bounce', 'Bounce'), ('flash', 'Flash'), ('pulse', 'Pulse'), ('rubberBand', 'Rubber Band'), ('shake', 'Shake'), ('swing', 'Swing'), ('tada', 'Ta-Da'), ('wobble', 'Wobble'), ('bounceIn', 'Bounce In'), ('bounceInDown', 'Bounce In Down'), ('bounceInLeft', 'Bounce In Left'), ('bounceInRight', 'Bounce In Right'), ('bounceInUp', 'Bounce In Up'), ('bounceOut', 'Bounce Out'), ('bounceOutDown', 'Bounce Out Down'), ('bounceOutLeft', 'Bounce Out Left'), ('bounceOutRight', 'Bounce Out Right'), ('bounceOutUp', 'Bounce Out Up'), ('fadeIn', 'Fade In'), ('fadeInDown', 'Fade In Down'), ('fadeInDownBig', 'Fade In Down Big'), ('fadeInLeft', 'Fade In Left'), ('fadeInLeftBig', 'Fade In Left Big'), ('fadeInRight', 'Fade In Right'), ('fadeInRightBig', 'Fade In Right Big'), ('fadeInUp', 'Fade In Up'), ('fadeInUpBig', 'Fade In Up Big'), ('fadeOut', 'Fade Out'), ('fadeOutDown', 'Fade Out Down'), ('fadeOutDownBig', 'Fade Out Down Big'), ('fadeOutLeft', 'Fade Out Left'), ('fadeOutLeftBig', 'Fade Out Left Big'), ('fadeOutRight', 'Fade Out Right'), ('fadeOutRightBig', 'Fade Out Right Big'), ('fadeOutUp', 'Fade Out Up'), ('fadeOutUpBig', 'Fade Out Up Big'), ('flipInX', 'Flip In X'), ('flipInY', 'Flip In Y'), ('flipOutX', 'Flip Out X'), ('flipOutY', 'Flip Out Y'), ('lightSpeedIn', 'Light Speed In'), ('lightSpeedOut', 'Light Speed Out'), ('rotateIn', 'Rotate In'), ('rotateInDownLeft', 'Rotate In Down Left'), ('rotateInDownRight', 'Rotate In Down Right'), ('rotateInUpLeft', 'Rotate In Up Left'), ('rotateInUpRight', 'Rotate In Up Right'), ('rotateOut', 'Rotate Out'), ('rotateOutDownLeft', 'Rotate Out Down Left'), ('rotateOutDownRight', 'Rotate Out Down Right'), ('rotateOutUpLeft', 'Rotate Out Up Left'), ('rotateOutUpRight', 'Rotate Out Up Right'), ('hinge', 'Hinge'), ('rollIn', 'Roll In'), ('rollOut', 'Roll Out'), ('zoomIn', 'Zoom In'), ('zoomInDown', 'Zoom Out'), ('zoomInLeft', 'Zoom In Left'), ('zoomInRight', 'Zoom In Right'), ('zoomInUp', 'Zoom In Up'), ('zoomOut', 'Zoom Out'), ('zoomOutDown', 'Zoom Out Down'), ('zoomOutLeft', 'Zoom Out Left'), ('zoomOutRight', 'Zoom Out Right'), ('zoomOutUp', 'Zoom Out Up'), ('slideInDown', 'Slide In Down'), ('slideInLeft', 'Slide In Left'), ('slideInRight', 'Slide In Right'), ('slideInUp', 'Slide In Up'), ('slideOutDown', 'Slide Out Down'), ('slideOutLeft', 'Slide Out Left'), ('slideOutRight', 'Slide Out Right'), ('slideOutUp', 'Slide Out Up')], max_length=25)),
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
                ('cmsplugin_ptr', models.OneToOneField(serialize=False, primary_key=True, parent_link=True, auto_created=True, to='cms.CMSPlugin')),
                ('animation_class', models.CharField(default='bounce', choices=[('bounce', 'Bounce'), ('flash', 'Flash'), ('pulse', 'Pulse'), ('rubberBand', 'Rubber Band'), ('shake', 'Shake'), ('swing', 'Swing'), ('tada', 'Ta-Da'), ('wobble', 'Wobble'), ('bounceIn', 'Bounce In'), ('bounceInDown', 'Bounce In Down'), ('bounceInLeft', 'Bounce In Left'), ('bounceInRight', 'Bounce In Right'), ('bounceInUp', 'Bounce In Up'), ('bounceOut', 'Bounce Out'), ('bounceOutDown', 'Bounce Out Down'), ('bounceOutLeft', 'Bounce Out Left'), ('bounceOutRight', 'Bounce Out Right'), ('bounceOutUp', 'Bounce Out Up'), ('fadeIn', 'Fade In'), ('fadeInDown', 'Fade In Down'), ('fadeInDownBig', 'Fade In Down Big'), ('fadeInLeft', 'Fade In Left'), ('fadeInLeftBig', 'Fade In Left Big'), ('fadeInRight', 'Fade In Right'), ('fadeInRightBig', 'Fade In Right Big'), ('fadeInUp', 'Fade In Up'), ('fadeInUpBig', 'Fade In Up Big'), ('fadeOut', 'Fade Out'), ('fadeOutDown', 'Fade Out Down'), ('fadeOutDownBig', 'Fade Out Down Big'), ('fadeOutLeft', 'Fade Out Left'), ('fadeOutLeftBig', 'Fade Out Left Big'), ('fadeOutRight', 'Fade Out Right'), ('fadeOutRightBig', 'Fade Out Right Big'), ('fadeOutUp', 'Fade Out Up'), ('fadeOutUpBig', 'Fade Out Up Big'), ('flipInX', 'Flip In X'), ('flipInY', 'Flip In Y'), ('flipOutX', 'Flip Out X'), ('flipOutY', 'Flip Out Y'), ('lightSpeedIn', 'Light Speed In'), ('lightSpeedOut', 'Light Speed Out'), ('rotateIn', 'Rotate In'), ('rotateInDownLeft', 'Rotate In Down Left'), ('rotateInDownRight', 'Rotate In Down Right'), ('rotateInUpLeft', 'Rotate In Up Left'), ('rotateInUpRight', 'Rotate In Up Right'), ('rotateOut', 'Rotate Out'), ('rotateOutDownLeft', 'Rotate Out Down Left'), ('rotateOutDownRight', 'Rotate Out Down Right'), ('rotateOutUpLeft', 'Rotate Out Up Left'), ('rotateOutUpRight', 'Rotate Out Up Right'), ('hinge', 'Hinge'), ('rollIn', 'Roll In'), ('rollOut', 'Roll Out'), ('zoomIn', 'Zoom In'), ('zoomInDown', 'Zoom Out'), ('zoomInLeft', 'Zoom In Left'), ('zoomInRight', 'Zoom In Right'), ('zoomInUp', 'Zoom In Up'), ('zoomOut', 'Zoom Out'), ('zoomOutDown', 'Zoom Out Down'), ('zoomOutLeft', 'Zoom Out Left'), ('zoomOutRight', 'Zoom Out Right'), ('zoomOutUp', 'Zoom Out Up'), ('slideInDown', 'Slide In Down'), ('slideInLeft', 'Slide In Left'), ('slideInRight', 'Slide In Right'), ('slideInUp', 'Slide In Up'), ('slideOutDown', 'Slide Out Down'), ('slideOutLeft', 'Slide Out Left'), ('slideOutRight', 'Slide Out Right'), ('slideOutUp', 'Slide Out Up')], max_length=25)),
                ('duration', models.PositiveSmallIntegerField(null=True, help_text='Change the animation duration')),
                ('delay', models.PositiveSmallIntegerField(null=True, help_text='Delay before the animation starts')),
                ('offset', models.PositiveSmallIntegerField(null=True, help_text='Distance to start the animation (related to the browser bottom)')),
                ('iteration', models.PositiveSmallIntegerField(null=True, help_text='Number of times the animation is repeated')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
