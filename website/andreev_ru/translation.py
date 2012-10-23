from modeltranslation.translator import translator, TranslationOptions
from andreev_ru.main.models import CustomPage, Work, Category

class CustomPageTranslationOptions(TranslationOptions):
    fields = ('title', 'content', )

class WorkTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )

class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', )

translator.register(CustomPage, CustomPageTranslationOptions) 
translator.register(Work, WorkTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
