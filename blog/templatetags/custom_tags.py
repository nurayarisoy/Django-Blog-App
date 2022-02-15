from django import template

register = template.Library()


@register.filter(name='cut')
def cut(value, arg):

    new_value = value.filter(post=arg)

    return new_value.count()
