from django import template
from django.utils.safestring import mark_safe

from andreev_ru.main import models

register = template.Library()

@register.filter
def translate(value, language):
    def _translate(v):
        if hasattr(v, '__iter__'):
            return [_translate(i) for i in v]
        else:
            return models.Translation(v, language)
    return _translate(value)