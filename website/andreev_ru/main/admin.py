from django.contrib import admin
from django import forms
from modeltranslation.admin import TranslationAdmin
from andreev_ru.main.forms import WorkForm, FlatpageForm, PersonForm, WorkImageForm
from andreev_ru.main.models import Work, WorkImage, Category, Person, Department

from django.contrib.flatpages.models import FlatPage

class WorkImageAdmin(admin.TabularInline):
    form = WorkImageForm
    template = 'admin/inlineimage.html'
    fields = ('image', 'position',)
    sortable_field_name = "position"
    model = WorkImage
    extra = 3

class WorkAdmin(TranslationAdmin):
    form = WorkForm
    list_display = ('title','description')
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ WorkImageAdmin, ]

    class Media:
        css = {'all': ['redactor_fix.css']}

class CategotyAdmin(TranslationAdmin):
    list_display = ('name',)

class CustomFlatPageAdmin(TranslationAdmin):
    list_display = ('title', 'url', )
    form = FlatpageForm

class PersonAdmin(TranslationAdmin):
    form = PersonForm
    list_display = ('name', 'bio', 'occupation')

class PositionAdmin(TranslationAdmin):
    list_display = ('name',)


admin.site.register(Work, WorkAdmin)
admin.site.register(Category, CategotyAdmin)

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, CustomFlatPageAdmin)

admin.site.register(Person, PersonAdmin)
admin.site.register(Department, PositionAdmin)
