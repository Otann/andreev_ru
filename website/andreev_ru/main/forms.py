from django.contrib import admin
from django import forms
from modeltranslation.admin import TranslationAdmin
from andreev_ru.main.models import Work, WorkImage, Category, Person, Department

from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld
from django.contrib.flatpages.admin import FlatpageForm as FlatpageFormOld

from redactor.widgets import RedactorEditor

class WorkImageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(WorkImageForm, self).__init__(*args, **kwargs)
        self.fields['position'].widget = forms.HiddenInput()

class WorkForm(forms.ModelForm):
    class Meta:
        model = Work
        widgets = {
            'description_ru': RedactorEditor(),
            'description_en': RedactorEditor(),
            }

class FlatpageForm(FlatpageFormOld):
    class Meta:
        model = FlatPage
        widgets = {
            'content_ru': RedactorEditor(),
            'content_en': RedactorEditor(),
            }

class PersonForm(forms.ModelForm):
    class Meta:
        model = Work
        widgets = {
            'bio_ru': RedactorEditor(),
            'bio_en': RedactorEditor(),
            }
