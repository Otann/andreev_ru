from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from andreev_ru.main.forms import *
from andreev_ru.main.models import *

from django.contrib.flatpages.models import FlatPage

class WorkImageAdmin(admin.TabularInline):
    fields = ('image', 'position',)
    sortable_field_name = "position"           # Required for grapelli's sortable
    form = WorkImageForm                       # Hides position field
    template = 'admin/inlineimage.html'        # Adds image preview
    model = WorkImage                          # Related model
    extra = 3                                  # Amount of additional tabular items

class WorkAdmin(TranslationAdmin):
    form = WorkForm                            # Add RedactorJS fields
    list_display = ('title','description')
    prepopulated_fields = {"slug": ("title",)} # Auto-populate based on russian title
    inlines = [ WorkImageAdmin, ]              # Inline add/remove for these

    class Media:
        css = {'all': ['redactor_fix.css']}

class CategoryAdmin(TranslationAdmin):
    list_display = ('name',)

class CustomPageAdmin(TranslationAdmin):
    list_display = ('title', 'position', 'slug',)
    list_editable = ('position', 'slug',)
    form = CustomPageForm                       # Add RedactorJS fields
    prepopulated_fields = {"slug": ("title",)}  # Auto-populate based on russian title

    class Media:
        css = {'all': ['redactor_fix.css']}     # Fix Redactor z-index overlapping
#        js  = [
#            'grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
#            'grappelli/tinymce_setup/tinymce_setup.js',
#            ]

class CustomStringAdmin(TranslationAdmin):
    list_display = ('key', 'value_ru', 'value_en',)
    list_editable = ('value_ru', 'value_en',)

class PersonAdmin(TranslationAdmin):
    list_display = ('name', 'bio', 'occupation')
    form = PersonForm                           # Add RedactorJS fields

    class Media:
        css = {'all': ['redactor_fix.css']}     # Fix Redactor z-index overlapping

class DepartmentAdmin(TranslationAdmin):
    list_display = ('name',)


admin.site.register(Work, WorkAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.register(CustomPage, CustomPageAdmin)
admin.site.register(CustomString, CustomStringAdmin)

admin.site.register(Person, PersonAdmin)
admin.site.register(Department, DepartmentAdmin)
