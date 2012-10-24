#!/usr/bin/env python
# coding: utf-8

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.utils.text import truncate_words
from django.utils.html import strip_tags

class CustomPage(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()

	slug = models.SlugField(max_length=200, unique=True)

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name = u'Страница'
		verbose_name_plural = u'Страницы'

class Category(models.Model):
	name = models.CharField(max_length=200)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = u'Категория'
		verbose_name_plural = u'Категории'

class Work(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()

	date_built = models.DateTimeField('Last updated date')
	categories = models.ManyToManyField(Category)

	slug = models.SlugField(max_length=200, unique=True)

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name = u'Объект'
		verbose_name_plural = u'Объекты'

class WorkImage(models.Model):
	work = models.ForeignKey(Work, related_name='images')
	image = models.ImageField(upload_to='work_image')
