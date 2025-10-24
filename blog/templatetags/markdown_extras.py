import markdown as md
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter()
@stringfilter
def markdown(value):
    """
    Convert markdown text to HTML
    """
    return mark_safe(md.markdown(value, extensions=['extra', 'nl2br', 'sane_lists']))

