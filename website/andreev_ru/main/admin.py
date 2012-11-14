from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from andreev_ru.main.forms import WorkForm, FlatpageForm, PersonForm, WorkImageForm
from andreev_ru.main.models import Work, WorkImage, Category, Person, Department

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

class CategotyAdmin(TranslationAdmin):
    list_display = ('name',)

class CustomFlatPageAdmin(TranslationAdmin):
    list_display = ('title', 'url', )
    form = FlatpageForm                         # Add RedactorJS fields

    class Media:
        css = {'all': ['redactor_fix.css']}     # Fix Redactor z-index overlapping

class PersonAdmin(TranslationAdmin):
    list_display = ('name', 'bio', 'occupation')
    form = PersonForm                           # Add RedactorJS fields

    class Media:
        css = {'all': ['redactor_fix.css']}     # Fix Redactor z-index overlapping

class PositionAdmin(TranslationAdmin):
    list_display = ('name',)


admin.site.register(Work, WorkAdmin)
admin.site.register(Category, CategotyAdmin)

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, CustomFlatPageAdmin)

admin.site.register(Person, PersonAdmin)
admin.site.register(Department, PositionAdmin)
