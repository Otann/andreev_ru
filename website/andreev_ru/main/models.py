#!/usr/bin/env python
# coding: utf-8

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 200)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Категория объекта'
        verbose_name_plural = u'Категории объектов'

class Work(models.Model):
    title = models.CharField(verbose_name = u'Название', max_length = 200)
    description = models.TextField(verbose_name = u'Описание')

    authors      = models.CharField(verbose_name = u'Авторы', max_length = 1024)
    address      = models.CharField(verbose_name = u'Адрес', max_length = 1024)
    release_year = models.IntegerField(verbose_name = u'Год(ы) завершени постройки')
    square       = models.IntegerField(verbose_name = u'Площадь')
    panorama_url = models.CharField(verbose_name = u'Ссылка на панораму', max_length = 1024)

#    date_built   = models.DateField(verbose_name = u'Когда сдано')
    categories   = models.ManyToManyField(Category, verbose_name = u'Категории')

    slug = models.SlugField(verbose_name = u'Относительный URL', max_length = 200, unique=True)

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

class Department(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Отдел'
        verbose_name_plural = u'Отделы'

class Person(models.Model):
    name       = models.CharField(verbose_name = u'ФИО', max_length = 1024)
    occupation = models.CharField(verbose_name = u'Род деятельности', max_length = 1024)
    bio        = models.TextField(verbose_name = u'История')
    image      = models.ImageField(verbose_name = u'Фотография', upload_to = 'team')

    position = models.ForeignKey(Department, verbose_name = u'Отдел')

    class Meta:
        verbose_name = u'Сотрудник'
        verbose_name_plural = u'Сотрудники'

class CustomPage(models.Model):
    title    = models.CharField(verbose_name = u'Заголовок', max_length = 1024)
    content  = models.TextField(verbose_name = u'Содержание')
    slug     = models.SlugField(verbose_name = u'Относительный URL', max_length = 200, unique=True)
    position = models.PositiveSmallIntegerField(verbose_name = u'Позиция в меню')

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
