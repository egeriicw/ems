# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Site'
        db.create_table(u'bedes_site', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('county', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('elevation', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=40)),
        ))
        db.send_create_signal(u'bedes', ['Site'])

        # Adding model 'ClimateZone'
        db.create_table(u'bedes_climatezone', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bedes.Site'])),
            ('zone', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'bedes', ['ClimateZone'])

        # Adding model 'SiteType'
        db.create_table(u'bedes_sitetype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bedes.Site'])),
            ('sitetype', self.gf('django.db.models.fields.CharField')(max_length=8)),
        ))
        db.send_create_signal(u'bedes', ['SiteType'])


    def backwards(self, orm):
        # Deleting model 'Site'
        db.delete_table(u'bedes_site')

        # Deleting model 'ClimateZone'
        db.delete_table(u'bedes_climatezone')

        # Deleting model 'SiteType'
        db.delete_table(u'bedes_sitetype')


    models = {
        u'bedes.climatezone': {
            'Meta': {'object_name': 'ClimateZone'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bedes.Site']"}),
            'zone': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'bedes.site': {
            'Meta': {'object_name': 'Site'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'county': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'elevation': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '40'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'bedes.sitetype': {
            'Meta': {'object_name': 'SiteType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bedes.Site']"}),
            'sitetype': ('django.db.models.fields.CharField', [], {'max_length': '8'})
        }
    }

    complete_apps = ['bedes']