# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'CustomPage.position'
        db.add_column('main_custompage', 'position',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'CustomPage.position'
        db.delete_column('main_custompage', 'position')


    models = {
        'main.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'main.custompage': {
            'Meta': {'object_name': 'CustomPage'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'content_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'content_ru': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'title_ru': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'})
        },
        'main.customstring': {
            'Meta': {'object_name': 'CustomString'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'value_en': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'value_ru': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'})
        },
        'main.department': {
            'Meta': {'object_name': 'Department'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'main.person': {
            'Meta': {'object_name': 'Person'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'bio_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'bio_ru': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'occupation': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'occupation_en': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'occupation_ru': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Department']"})
        },
        'main.work': {
            'Meta': {'object_name': 'Work'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'address_en': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'address_ru': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'authors': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'authors_en': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'authors_ru': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['main.Category']", 'symmetrical': 'False'}),
            'date_built': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'description_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_ru': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'panorama_url': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'release_year': ('django.db.models.fields.IntegerField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '200'}),
            'square': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'title_ru': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'main.workimage': {
            'Meta': {'ordering': "['position']", 'object_name': 'WorkImage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'work': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': "orm['main.Work']"})
        }
    }

    complete_apps = ['main']