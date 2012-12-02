from modeltranslation.translator import translator, TranslationOptions
from andreev_ru.main.models import *

class CustomPageTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)

class CustomStringTranslationOptions(TranslationOptions):
    fields = ('value',)

class WorkTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'authors', 'address',)

class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', )

class PositionTranslationOptions(TranslationOptions):
    fields = ('name', )

class PersonTranslationOptions(TranslationOptions):
    fields = ('name', 'bio', 'occupation')

translator.register(CustomPage, CustomPageTranslationOptions)
translator.register(CustomString, CustomStringTranslationOptions)

translator.register(Category, CategoryTranslationOptions)
translator.register(Work, WorkTranslationOptions)

translator.register(Department, PositionTranslationOptions)
translator.register(Person, PersonTranslationOptions)
