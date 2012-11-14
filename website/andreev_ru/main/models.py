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
    title = models.CharField(max_length = 200, verbose_name = u'Название')
    description = models.TextField(verbose_name = u'Описание')

    authors      = models.CharField(max_length = 1024, verbose_name = u'Авторы')
    address      = models.CharField(max_length = 1024, verbose_name = u'Адрес')
    release_year = models.IntegerField(verbose_name = u'Год завершени постройки')
    square       = models.IntegerField(verbose_name = u'Площадь')
    panorama_url = models.CharField(max_length = 1024, verbose_name = u'Ссылка на панораму')

    date_built   = models.DateField(verbose_name = u'Когда сдано')
    categories   = models.ManyToManyField(Category, verbose_name = u'Категории')

    slug = models.SlugField(max_length = 200, unique=True, verbose_name = u'Относительный URL')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'Объект'
        verbose_name_plural = u'Объекты'

class WorkImage(models.Model):
    work     = models.ForeignKey(Work, related_name = 'images', verbose_name = u'Фотографии')
    image    = models.ImageField(upload_to = 'works', verbose_name = u'Файл')
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
    name       = models.CharField(max_length = 1024, verbose_name = u'ФИО')
    occupation = models.CharField(max_length = 1024, verbose_name = u'Род деятельности')
    bio        = models.TextField(verbose_name = u'История')
    image      = models.ImageField(upload_to = 'team', verbose_name = u'Фотография')

    position = models.ForeignKey(Department, verbose_name = u'Отдел')

    class Meta:
        verbose_name = u'Сотрудник'
        verbose_name_plural = u'Сотрудники'