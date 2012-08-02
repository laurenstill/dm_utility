# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'DailyVitals.low_bgl'
        db.delete_column('chart_dailyvitals', 'low_bgl')

        # Deleting field 'DailyVitals.high_bgl'
        db.delete_column('chart_dailyvitals', 'high_bgl')

        # Adding field 'DailyVitals.high_BGL'
        db.add_column('chart_dailyvitals', 'high_BGL',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'DailyVitals.low_BGL'
        db.add_column('chart_dailyvitals', 'low_BGL',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'DailyVitals.low_bgl'
        db.add_column('chart_dailyvitals', 'low_bgl',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'DailyVitals.high_bgl'
        db.add_column('chart_dailyvitals', 'high_bgl',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'DailyVitals.high_BGL'
        db.delete_column('chart_dailyvitals', 'high_BGL')

        # Deleting field 'DailyVitals.low_BGL'
        db.delete_column('chart_dailyvitals', 'low_BGL')


    models = {
        'chart.dailyvitals': {
            'Meta': {'object_name': 'DailyVitals'},
            'activity': ('django.db.models.fields.IntegerField', [], {}),
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'diastolic': ('django.db.models.fields.IntegerField', [], {}),
            'diet': ('django.db.models.fields.IntegerField', [], {}),
            'entered_at': ('django.db.models.fields.DateTimeField', [], {}),
            'high_BGL': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'low_BGL': ('django.db.models.fields.IntegerField', [], {}),
            'medications': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'mood': ('django.db.models.fields.IntegerField', [], {}),
            'systolic': ('django.db.models.fields.IntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chart.User']"}),
            'weight': ('django.db.models.fields.IntegerField', [], {})
        },
        'chart.user': {
            'Meta': {'object_name': 'User'},
            'birthday': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'registered_date': ('django.db.models.fields.DateTimeField', [], {}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['chart']