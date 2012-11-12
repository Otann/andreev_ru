from django.contrib import admin
from django import forms
from modeltranslation.admin import TranslationAdmin
from andreev_ru.main.models import Work, WorkImage, Category

from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld
from django.contrib.flatpages.admin import FlatpageForm as FlatpageFormOld

from redactor.widgets import RedactorEditor


class WorkForm(forms.ModelForm):
    class Meta:
        model = Work
        widgets = {
            'description_ru': RedactorEditor(),
            'description_en': RedactorEditor(),
            }

class WorkImageAdmin(admin.TabularInline):
    model = WorkImage
    extra = 3

class WorkAdmin(TranslationAdmin):
    form = WorkForm
    list_display = ('title','description')
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ WorkImageAdmin, ]

class CategotyAdmin(TranslationAdmin):
    list_display = ('name',)

class FlatpageForm(FlatpageFormOld):
    class Meta:
        model = FlatPage
        widgets = {
            'content_ru': RedactorEditor(),
            'content_en': RedactorEditor(),
        }

class CustomFlatPageAdmin(TranslationAdmin):
    list_display = ('title', 'url', )
    form = FlatpageForm

admin.site.register(Work, WorkAdmin)
admin.site.register(Category, CategotyAdmin)

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, CustomFlatPageAdmin)
