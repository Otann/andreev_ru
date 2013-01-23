from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from andreev_ru.main.models import *
from andreev_ru.main.forms import WorkImageForm
from image_cropping import ImageCroppingMixin

class WorkImageAdmin(admin.TabularInline):
    fields = ('image', 'position',)
    sortable_field_name = "position"           # Required for grapelli's sortable
    form = WorkImageForm                       # Hides position field
    template = 'admin/inlineimage.html'        # Adds image preview
    model = WorkImage                          # Related model
    extra = 3                                  # Amount of additional tabular items

class WorkAuthorsAdmin(admin.TabularInline):
    fields = ('title_ru', 'title_en', 'names_ru', 'names_en',)
    model = WorkAuthors                        # Related model
    extra = 3                                  # Amount of additional tabular items

class WorkAdmin(ImageCroppingMixin, TranslationAdmin):
    list_display = ('title','description')
    inlines = [ WorkAuthorsAdmin, WorkImageAdmin, ] # Inline add/remove for these
    prepopulated_fields = {"slug": ("title",)}    # Auto-populate based on russian title

    class Media:
        css = {'all': ['redactor_fix.css']}

class CategoryAdmin(TranslationAdmin):
    list_display = ('id', 'name_ru', 'name_en',)
    list_editable = ('name_ru', 'name_en',)

class CustomPageAdmin(TranslationAdmin):
    list_display = ('title', 'position', 'slug',)
    list_editable = ('position', 'slug',)
    prepopulated_fields = {"slug": ("title",)}  # Auto-populate based on russian title

class CustomStringAdmin(TranslationAdmin):
    list_display = ('key', 'value_ru', 'value_en',)
    list_editable = ('value_ru', 'value_en',)

class PersonAdmin(TranslationAdmin):
    list_display = ('name', 'bio', 'occupation')

class DepartmentAdmin(TranslationAdmin):
    list_display = ('id', 'name_ru', 'name_en',)
    list_editable = ('name_ru', 'name_en',)

class NewsAdmin(TranslationAdmin):
    list_display = ('title', 'content', 'pub_date')
    prepopulated_fields = {"slug": ("title",)}  # Auto-populate based on russian title


admin.site.register(Work, WorkAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.register(News, NewsAdmin)
admin.site.register(CustomPage, CustomPageAdmin)
admin.site.register(CustomString, CustomStringAdmin)

admin.site.register(Person, PersonAdmin)
admin.site.register(Department, DepartmentAdmin)
