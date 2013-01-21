from modeltranslation.translator import translator, TranslationOptions
from andreev_ru.main.models import *

class CustomPageTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)
translator.register(CustomPage, CustomPageTranslationOptions)

class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'content')
translator.register(News, NewsTranslationOptions)

class CustomStringTranslationOptions(TranslationOptions):
    fields = ('value',)
translator.register(CustomString, CustomStringTranslationOptions)

class WorkTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'address', 'client')
translator.register(Work, WorkTranslationOptions)

class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', )
translator.register(Category, CategoryTranslationOptions)

class DepartmentTranslationOptions(TranslationOptions):
    fields = ('name', )
translator.register(Department, DepartmentTranslationOptions)

class PersonTranslationOptions(TranslationOptions):
    fields = ('name', 'bio', 'occupation')
translator.register(Person, PersonTranslationOptions)

class AuthorsTranslationOptions(TranslationOptions):
    fields = ('title', 'names')
translator.register(WorkAuthors, AuthorsTranslationOptions)
