from datetime import datetime, timedelta
from pprint import pprint

from django import template

register = template.Library()


@register.filter(name='is_allowed')
def is_allowed(value):
    # Eligible
    now_date = datetime.now().date()
    delta = now_date - value
    years = delta.days / 365

    if years > 13:
        return "allowed"
    else:
        return "blocked"

@register.filter(name='bizzfuzz')
def bizzfuzz(value):
    result = ""

    if value % 3 == 0:
        result += "Bizz"
    if value % 5 == 0:
        result += "Fuzz"

    return result