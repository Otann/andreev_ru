from modeltranslation.translator import translator, TranslationOptions
from andreev_ru.main.models import Work, Category
from django.contrib.flatpages.models import FlatPage

class CustomPageTranslationOptions(TranslationOptions):
    fields = ('title', 'content', )

class WorkTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'authors', 'address',)

class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', )

class FlatPageTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)

translator.register(Work, WorkTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
translator.register(FlatPage, FlatPageTranslationOptions)
