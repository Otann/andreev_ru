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

    slug = models.SlugField(u'Относительный URL', max_length = 200, unique=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'Объект'
        verbose_name_plural = u'Объекты'

class WorkImage(models.Model):
    work  = models.ForeignKey(Work, related_name = 'images', verbose_name = u'Фотографии')
    image = models.ImageField(upload_to = 'work_image')

class Position(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Должность'
        verbose_name_plural = u'Должности'

class Person(models.Model):
    name = models.CharField(max_length = 1024, verbose_name = u'ФИО')
    bio  = models.TextField(verbose_name = u'История')

    position = models.ForeignKey(Position)

    class Meta:
        verbose_name = u'Сотрудник'
        verbose_name_plural = u'Сотрудники'
