# myapp/templatetags/custom_filters.py

import re
from django import template

register = template.Library()

@register.filter
def extract_parentheses(value):
    match = re.search(r'\((.*?)\)', value)
    return match.group(1) if match else ''
