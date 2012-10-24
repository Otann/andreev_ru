from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from andreev_ru.main.models import CustomPage, Work, WorkImage, Category

class WorkImageAdmin(admin.TabularInline):
    model = WorkImage
    extra = 3

class WorkAdmin(TranslationAdmin):
    list_display = ('title','description')
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ WorkImageAdmin, ]

class CategotyAdmin(TranslationAdmin):
    list_display = ('name',)

class CustomPageAdmin(TranslationAdmin):
    list_display = ('title','content')
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Work, WorkAdmin)
admin.site.register(Category, CategotyAdmin)
admin.site.register(CustomPage, CustomPageAdmin)
