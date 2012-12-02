from django.contrib import admin
from django import forms
from modeltranslation.admin import TranslationAdmin
from andreev_ru.main.models import Work, CustomPage

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

class CustomPageForm(forms.ModelForm):
    class Meta:
        model = CustomPage
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
