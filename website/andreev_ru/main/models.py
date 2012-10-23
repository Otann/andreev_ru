from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.utils.text import truncate_words
from django.utils.html import strip_tags
from django.utils.functional import curry
from django.utils.translation import ugettext_lazy as _

## Main Models
########################

class Page(models.Model):
	
	title = models.CharField(max_length=200)
	content = models.TextField()

	last_updated = models.DateTimeField('Last updated date')

	def __unicode__(self):
		return self.title_ru

class Work(models.Model):
	title_ru = models.CharField(max_length=200)
	title_en = models.CharField(max_length=200)

	description_ru = models.TextField()
	description_en = models.TextField()

	date_built = models.DateTimeField('Last updated date')

	def __unicode__(self):
		return self.title_ru

## Helpers
########################

class Translation(object):
	def __init__(self, obj, language):
		super(Translation, self).__init__()
		self.obj = obj
		self.language = language

	def __getattr__(self, name):
		attr = getattr(self.obj, name)
		if getattr(attr, 'needs_language', None):
			attr = curry(attr, self.language)
		return attr