from modeltranslation.translator import translator, TranslationOptions
from andreev_ru.main.models import Work, Category, Person, Department
from django.contrib.flatpages.models import FlatPage

class FlatPageTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)

class WorkTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'authors', 'address',)

class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', )

class PositionTranslationOptions(TranslationOptions):
    fields = ('name', )

class PersonTranslationOptions(TranslationOptions):
    fields = ('name', 'bio', 'occupation')

translator.register(FlatPage, FlatPageTranslationOptions)

translator.register(Category, CategoryTranslationOptions)
translator.register(Work, WorkTranslationOptions)

translator.register(Department, PositionTranslationOptions)
translator.register(Person, PersonTranslationOptions)
