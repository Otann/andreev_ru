# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Person.bio'
        db.alter_column('main_person', 'bio', self.gf('ckeditor.fields.RichTextField')())

        # Changing field 'Person.bio_en'
        db.alter_column('main_person', 'bio_en', self.gf('ckeditor.fields.RichTextField')(null=True))

        # Changing field 'Person.bio_ru'
        db.alter_column('main_person', 'bio_ru', self.gf('ckeditor.fields.RichTextField')(null=True))
        # Adding field 'Work.client'
        db.add_column('main_work', 'client',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=1024, blank=True),
                      keep_default=False)


        # Changing field 'Work.description'
        db.alter_column('main_work', 'description', self.gf('ckeditor.fields.RichTextField')())

        # Changing field 'Work.description_en'
        db.alter_column('main_work', 'description_en', self.gf('ckeditor.fields.RichTextField')(null=True))

        # Changing field 'Work.panorama_url'
        db.alter_column('main_work', 'panorama_url', self.gf('django.db.models.fields.URLField')(max_length=1024))

        # Changing field 'Work.description_ru'
        db.alter_column('main_work', 'description_ru', self.gf('ckeditor.fields.RichTextField')(null=True))

        # Changing field 'Work.release_year'
        db.alter_column('main_work', 'release_year', self.gf('django.db.models.fields.CharField')(max_length=1024))

        # Changing field 'CustomPage.content_en'
        db.alter_column('main_custompage', 'content_en', self.gf('ckeditor.fields.RichTextField')(null=True))

        # Changing field 'CustomPage.content_ru'
        db.alter_column('main_custompage', 'content_ru', self.gf('ckeditor.fields.RichTextField')(null=True))

        # Changing field 'CustomPage.content'
        db.alter_column('main_custompage', 'content', self.gf('ckeditor.fields.RichTextField')())

    def backwards(self, orm):

        # Changing field 'Person.bio'
        db.alter_column('main_person', 'bio', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Person.bio_en'
        db.alter_column('main_person', 'bio_en', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Person.bio_ru'
        db.alter_column('main_person', 'bio_ru', self.gf('django.db.models.fields.TextField')(null=True))
        # Deleting field 'Work.client'
        db.delete_column('main_work', 'client')


        # Changing field 'Work.description'
        db.alter_column('main_work', 'description', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Work.description_en'
        db.alter_column('main_work', 'description_en', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Work.panorama_url'
        db.alter_column('main_work', 'panorama_url', self.gf('django.db.models.fields.CharField')(max_length=1024))

        # Changing field 'Work.description_ru'
        db.alter_column('main_work', 'description_ru', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Work.release_year'
        db.alter_column('main_work', 'release_year', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'CustomPage.content_en'
        db.alter_column('main_custompage', 'content_en', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'CustomPage.content_ru'
        db.alter_column('main_custompage', 'content_ru', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'CustomPage.content'
        db.alter_column('main_custompage', 'content', self.gf('django.db.models.fields.TextField')())

    models = {
        'main.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'main.custompage': {
            'Meta': {'ordering': "('position',)", 'object_name': 'CustomPage'},
            'content': ('ckeditor.fields.RichTextField', [], {}),
            'content_en': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'content_ru': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
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
            'bio': ('ckeditor.fields.RichTextField', [], {}),
            'bio_en': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'bio_ru': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
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
            'address': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'address_en': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'address_ru': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'authors': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'authors_en': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'authors_ru': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['main.Category']", 'symmetrical': 'False', 'blank': 'True'}),
            'client': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'description': ('ckeditor.fields.RichTextField', [], {'blank': 'True'}),
            'description_en': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'description_ru': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'panorama_url': ('django.db.models.fields.URLField', [], {'max_length': '1024', 'blank': 'True'}),
            'release_year': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '200'}),
            'square': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
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