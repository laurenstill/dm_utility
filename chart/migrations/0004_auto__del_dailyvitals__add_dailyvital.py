# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'DailyVitals'
        db.delete_table('chart_dailyvitals')

        # Adding model 'DailyVital'
        db.create_table('chart_dailyvital', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('entered_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chart.User'])),
            ('high_BGL', self.gf('django.db.models.fields.IntegerField')()),
            ('low_BGL', self.gf('django.db.models.fields.IntegerField')()),
            ('diet', self.gf('django.db.models.fields.IntegerField')()),
            ('activity', self.gf('django.db.models.fields.IntegerField')()),
            ('mood', self.gf('django.db.models.fields.IntegerField')()),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('weight', self.gf('django.db.models.fields.IntegerField')()),
            ('systolic', self.gf('django.db.models.fields.IntegerField')()),
            ('diastolic', self.gf('django.db.models.fields.IntegerField')()),
            ('medications', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal('chart', ['DailyVital'])


    def backwards(self, orm):
        # Adding model 'DailyVitals'
        db.create_table('chart_dailyvitals', (
            ('low_BGL', self.gf('django.db.models.fields.IntegerField')()),
            ('weight', self.gf('django.db.models.fields.IntegerField')()),
            ('diet', self.gf('django.db.models.fields.IntegerField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chart.User'])),
            ('high_BGL', self.gf('django.db.models.fields.IntegerField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('medications', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('mood', self.gf('django.db.models.fields.IntegerField')()),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('systolic', self.gf('django.db.models.fields.IntegerField')()),
            ('entered_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('activity', self.gf('django.db.models.fields.IntegerField')()),
            ('diastolic', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('chart', ['DailyVitals'])

        # Deleting model 'DailyVital'
        db.delete_table('chart_dailyvital')


    models = {
        'chart.dailyvital': {
            'Meta': {'object_name': 'DailyVital'},
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