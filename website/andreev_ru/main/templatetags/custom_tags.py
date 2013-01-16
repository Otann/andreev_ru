# -*- coding: utf-8 -*-

import re
import trans

from django import template
from django.template.defaultfilters import stringfilter
from django.core.exceptions import ObjectDoesNotExist
from andreev_ru.main.models import CustomString

register = template.Library()

PUNCT_RE = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')

@register.filter(is_safe=True)
@stringfilter
def transliterate(value, delim=u'-'):
    return value.lower().encode('trans/slug')

@register.tag(name="custom_string")
def custom_string(parser, token):
    """Loads CustomString with key"""
    tag_name, tag_param = token.split_contents()
    key = tag_param[1:-1]
    try:
        object = CustomString.objects.get(key=key)
        return CustomStringNode(object.value)
    except ObjectDoesNotExist:
        return CustomStringNode(key)

class CustomStringNode(template.Node):
    def __init__(self, value):
        self.value = value
    def render(self, context):
        return self.value
