from django import template
import random

register = template.Library()

@register.filter
def random_image(lst):
    lst = list(lst.split(','))
    return random.choice(lst)