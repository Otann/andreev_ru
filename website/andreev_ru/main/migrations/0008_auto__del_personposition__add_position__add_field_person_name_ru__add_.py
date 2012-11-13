# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'PersonPosition'
        db.delete_table('main_personposition')

        # Adding model 'Position'
        db.create_table('main_position', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('name_ru', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('main', ['Position'])

        # Adding field 'Person.name_ru'
        db.add_column('main_person', 'name_ru',
                      self.gf('django.db.models.fields.CharField')(max_length=1024, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Person.name_en'
        db.add_column('main_person', 'name_en',
                      self.gf('django.db.models.fields.CharField')(max_length=1024, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Person.bio_ru'
        db.add_column('main_person', 'bio_ru',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Person.bio_en'
        db.add_column('main_person', 'bio_en',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


        # Changing field 'Person.position'
        db.alter_column('main_person', 'position_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Position']))

    def backwards(self, orm):
        # Adding model 'PersonPosition'
        db.create_table('main_personposition', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('main', ['PersonPosition'])

        # Deleting model 'Position'
        db.delete_table('main_position')

        # Deleting field 'Person.name_ru'
        db.delete_column('main_person', 'name_ru')

        # Deleting field 'Person.name_en'
        db.delete_column('main_person', 'name_en')

        # Deleting field 'Person.bio_ru'
        db.delete_column('main_person', 'bio_ru')

        # Deleting field 'Person.bio_en'
        db.delete_column('main_person', 'bio_en')


        # Changing field 'Person.position'
        db.alter_column('main_person', 'position_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.PersonPosition']))

    models = {
        'main.category': {
            'Meta': {'object_name': 'Category'},
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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Position']"})
        },
        'main.position': {
            'Meta': {'object_name': 'Position'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
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
            'Meta': {'object_name': 'WorkImage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'work': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': "orm['main.Work']"})
        }
    }

    complete_apps = ['main']