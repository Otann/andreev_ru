from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from andreev_ru.main.models import Page, Work

class PageAdmin(TranslationAdmin):
    list_display = ('title','content')

admin.site.register(Page, PageAdmin)
admin.site.register(Work)
