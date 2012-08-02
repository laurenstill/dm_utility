# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'User'
        db.delete_table('chart_user')

        # Adding model 'UserProfile'
        db.create_table('chart_userprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('birthday', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.utcnow)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=15)),
        ))
        db.send_create_signal('chart', ['UserProfile'])


        # Changing field 'DailyVital.user'
        db.alter_column('chart_dailyvital', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

    def backwards(self, orm):
        # Adding model 'User'
        db.create_table('chart_user', (
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('registered_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('birthday', self.gf('django.db.models.fields.DateField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('chart', ['User'])

        # Deleting model 'UserProfile'
        db.delete_table('chart_userprofile')


        # Changing field 'DailyVital.user'
        db.alter_column('chart_dailyvital', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chart.User']))

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
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
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'weight': ('django.db.models.fields.IntegerField', [], {})
        },
        'chart.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'birthday': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.utcnow'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['chart']