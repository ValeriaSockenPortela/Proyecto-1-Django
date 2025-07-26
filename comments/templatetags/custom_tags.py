from django import template
register = template.Library()
@register.simple_tag(name="my_connection")
def connection_db():
    return

@register.filter(name='my_name')
def name(value):
    return value