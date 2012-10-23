from modeltranslation.translator import translator, TranslationOptions
from andreev_ru.main.models import Page

class PageTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)

translator.register(Page, PageTranslationOptions)