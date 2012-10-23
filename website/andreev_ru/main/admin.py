from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from andreev_ru.main.models import CustomPage, Work, Category

class WorkAdmin(TranslationAdmin):
    list_display = ('title','description')

class CategotyAdmin(TranslationAdmin):
    list_display = ('name',)

class CustomPageAdmin(TranslationAdmin):
    list_display = ('title','content')

admin.site.register(Work, WorkAdmin)
admin.site.register(Category, CategotyAdmin)
admin.site.register(CustomPage, CustomPageAdmin)
