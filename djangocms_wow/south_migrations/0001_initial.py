# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Animation'
        db.create_table('djangocms_wow_animation', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(primary_key=True, to=orm['cms.CMSPlugin'], unique=True)),
            ('animation_class', self.gf('django.db.models.fields.CharField')(max_length=25, default='bounce')),
            ('infinite', self.gf('django.db.models.fields.NullBooleanField')(blank=True, null=True)),
        ))
        db.send_create_signal('djangocms_wow', ['Animation'])

        # Adding model 'WOWAnimation'
        db.create_table('djangocms_wow_wowanimation', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(primary_key=True, to=orm['cms.CMSPlugin'], unique=True)),
            ('animation_class', self.gf('django.db.models.fields.CharField')(max_length=25, default='bounce')),
            ('duration', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True)),
            ('delay', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True)),
            ('offset', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True)),
            ('iteration', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True)),
        ))
        db.send_create_signal('djangocms_wow', ['WOWAnimation'])


    def backwards(self, orm):
        # Deleting model 'Animation'
        db.delete_table('djangocms_wow_animation')

        # Deleting model 'WOWAnimation'
        db.delete_table('djangocms_wow_wowanimation')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '15'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'to': "orm['cms.CMSPlugin']"}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['cms.Placeholder']"}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True', 'null': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255'})
        },
        'djangocms_wow.animation': {
            'Meta': {'_ormbases': ['cms.CMSPlugin'], 'object_name': 'Animation'},
            'animation_class': ('django.db.models.fields.CharField', [], {'max_length': '25', 'default': "'bounce'"}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'primary_key': 'True', 'to': "orm['cms.CMSPlugin']", 'unique': 'True'}),
            'infinite': ('django.db.models.fields.NullBooleanField', [], {'blank': 'True', 'null': 'True'})
        },
        'djangocms_wow.wowanimation': {
            'Meta': {'_ormbases': ['cms.CMSPlugin'], 'object_name': 'WOWAnimation'},
            'animation_class': ('django.db.models.fields.CharField', [], {'max_length': '25', 'default': "'bounce'"}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'primary_key': 'True', 'to': "orm['cms.CMSPlugin']", 'unique': 'True'}),
            'delay': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'duration': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'iteration': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'offset': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'})
        }
    }

    complete_apps = ['djangocms_wow']