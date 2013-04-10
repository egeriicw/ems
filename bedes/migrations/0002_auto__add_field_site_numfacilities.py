# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Site.numfacilities'
        db.add_column(u'bedes_site', 'numfacilities',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Site.numfacilities'
        db.delete_column(u'bedes_site', 'numfacilities')


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
            'numfacilities': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
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