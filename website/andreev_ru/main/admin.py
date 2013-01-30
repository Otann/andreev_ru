from django.contrib import admin
from django import forms
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.safestring import mark_safe
from modeltranslation.admin import TranslationAdmin
from andreev_ru.main.models import *
from andreev_ru.main.forms import WorkImageForm
from image_cropping import ImageCroppingMixin


class AdminImageFieldWithThumbWidget(AdminFileWidget):
    def __init__(self, thumb_width=50, thumb_height=50, **kwargs):
        self.width = thumb_width
        self.height = thumb_height
        super(AdminImageFieldWithThumbWidget, self).__init__({})

    def render(self, name, value, attrs=None):
        thumb_html = ''
        if value and hasattr(value, "url"):
            thumb_html = '<img src="%s" width="%s" width="%s"/>' % (value.url, self.width, self.height)
        return mark_safe("%s%s" % (thumb_html, super(AdminImageFieldWithThumbWidget, self).render(name, value, attrs)))


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
    list_display = ('title', 'description')
    inlines = [WorkAuthorsAdmin, WorkImageAdmin]  # Inline add/remove for these
    prepopulated_fields = {"slug": ("title",)}    # Auto-populate based on russian title

    class Media:
        css = {'all': ['redactor_fix.css']}
admin.site.register(Work, WorkAdmin)


class CategoryAdmin(TranslationAdmin):
    list_display = ('id', 'name_ru', 'name_en',)
    list_editable = ('name_ru', 'name_en',)
admin.site.register(Category, CategoryAdmin)


class CustomPageAdmin(TranslationAdmin):
    list_display = ('title', 'position', 'slug',)
    list_editable = ('position', 'slug',)
    prepopulated_fields = {"slug": ("title",)}  # Auto-populate based on russian title
admin.site.register(CustomPage, CustomPageAdmin)


class CustomStringAdmin(TranslationAdmin):
    list_display = ('key', 'value_ru', 'value_en',)
    list_editable = ('value_ru', 'value_en',)
admin.site.register(CustomString, CustomStringAdmin)


class PersonAdmin(TranslationAdmin):
    list_display = ('name', 'bio', 'occupation')
admin.site.register(Person, PersonAdmin)


class DepartmentAdmin(TranslationAdmin):
    list_display = ('id', 'name_ru', 'name_en',)
    list_editable = ('name_ru', 'name_en',)
admin.site.register(Department, DepartmentAdmin)


class NewsAdmin(TranslationAdmin):
    list_display = ('title', 'content', 'pub_date')
    prepopulated_fields = {"slug": ("title",)}  # Auto-populate based on russian title
admin.site.register(News, NewsAdmin)


class TimelineIconAdmin(TranslationAdmin):
    list_display = ('title_ru', 'title_en', 'position', 'icon', 'work')
    list_editable = ('position',)

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'image' or db_field.name == 'icon':
            return forms.CharField(widget=AdminImageFieldWithThumbWidget(**kwargs))
        return super(TimelineIconAdmin, self).formfield_for_dbfield(db_field, **kwargs)
admin.site.register(TimelineIcon, TimelineIconAdmin)
