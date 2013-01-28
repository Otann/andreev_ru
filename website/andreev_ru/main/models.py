#!/usr/bin/env python
# coding: utf-8

from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from image_cropping import ImageRatioField

class Category(models.Model):
    name = models.CharField(max_length = 200)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Категория объекта'
        verbose_name_plural = u'Категории объектов'

class Work(models.Model):
    title = models.CharField(verbose_name = u'Название', max_length = 200)
    description = RichTextField(verbose_name = u'Описание', blank=True)

    client       = models.CharField(verbose_name = u'Заказчик', max_length = 1024, blank=True)
    address      = models.CharField(verbose_name = u'Адрес', max_length = 1024, blank=True)
    panorama_url = models.URLField(verbose_name = u'Ссылка на панораму', max_length = 1024, blank=True)

    build_start  = models.DateField(verbose_name = u'Начало строительства', blank = True, null = True)
    build_finish = models.DateField(verbose_name = u'Окончание строительства', blank = True, null = True)

    square       = models.IntegerField(verbose_name = u'Площадь', blank=True, null = True)

    categories   = models.ManyToManyField(Category, verbose_name = u'Категории', blank=True)

    slug  = models.SlugField(verbose_name = u'Относительный URL', max_length = 200, unique=True)

    image = models.ImageField(verbose_name = u'Миниатюра объекта', blank=True, null=True, upload_to='uploaded_images')
    thumb = ImageRatioField('image', '300x300')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'Объект'
        verbose_name_plural = u'Объекты'

class WorkImage(models.Model):
    work     = models.ForeignKey(Work, verbose_name = u'Фотографии', related_name = 'images')
    image    = models.ImageField(verbose_name = u'Файл', upload_to = 'works')
    position = models.PositiveSmallIntegerField(verbose_name = u'Позиция в слайдре')

    def __unicode__(self):
        return str(self.position)

    class Meta:
        ordering = ['position']
        verbose_name = u'Фотография объекта'
        verbose_name_plural = u'Фотографии объекта'

class WorkAuthors(models.Model):
    work  = models.ForeignKey(Work, verbose_name = u'Группы авторов', related_name = 'authors')
    title = models.CharField(max_length=200, verbose_name = u'Название группы')
    names = models.CharField(max_length=200, verbose_name = u'Фамилии и имена')

    class Meta:
        verbose_name = u'Группа авторов проекта'
        verbose_name_plural = u'Группы авторов проекта'


class Department(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Отдел'
        verbose_name_plural = u'Отделы'

class Person(models.Model):
    name       = models.CharField(verbose_name = u'ФИО', max_length = 1024)
    occupation = models.CharField(verbose_name = u'Род деятельности', max_length = 1024, blank=True)
    bio        = RichTextField(verbose_name = u'История', blank=True)
    image      = models.ImageField(verbose_name = u'Фотография', upload_to = 'team')

    position   = models.ForeignKey(Department, verbose_name = u'Отдел')

    class Meta:
        verbose_name = u'Сотрудник'
        verbose_name_plural = u'Сотрудники'

class News(models.Model):
    title       = models.CharField(verbose_name = u'Заголовок', max_length = 1024)
    content     = RichTextField(verbose_name = u'Содержание')
    slug        = models.SlugField(verbose_name = u'Относительный URL', max_length = 200, unique=True)
    pub_date    = models.DateTimeField(verbose_name = u'Дата публикации', default = datetime.now)
    is_featured = models.BooleanField(verbose_name = u'Показывать на главной?')

    class Meta:
        verbose_name = u'Новость'
        verbose_name_plural = u'Новости'

class CustomPage(models.Model):
    title    = models.CharField(verbose_name = u'Заголовок', max_length = 1024)
    content  = RichTextField(verbose_name = u'Содержание')
    slug     = models.SlugField(verbose_name = u'Относительный URL', max_length = 200, unique=True)
    position = models.PositiveSmallIntegerField(verbose_name = u'Позиция в меню', default = 0)
    is_shown = models.BooleanField(verbose_name = u'Показывать в меню?', default = True)

    class Meta:
        verbose_name = u'Страница Сайта'
        verbose_name_plural = u'Страницы Сайта'
        ordering = ('position',)

class CustomString(models.Model):
    value = models.CharField(verbose_name = u'Значение', max_length = 1024)
    key   = models.CharField(verbose_name = u'Ключ', max_length = 1024)

    class Meta:
        verbose_name = u'Дополнительные сведения'
        verbose_name_plural = u'Дополнительные сведения'
