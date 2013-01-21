#from django.contrib import admin
from django import forms
#from modeltranslation.admin import TranslationAdmin
#from andreev_ru.main.models import Work, CustomPage

class WorkImageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(WorkImageForm, self).__init__(*args, **kwargs)
        self.fields['position'].widget = forms.HiddenInput()
