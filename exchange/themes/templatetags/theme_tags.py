from django import template
from exchange.themes.models import Theme

register = template.Library()


@register.assignment_tag
def get_theme():
    try:
        theme = Theme.objects.get(active_theme=True)
    except Theme.DoesNotExist:
        theme = None
    return theme
