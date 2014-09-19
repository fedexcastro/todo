from django import template

register = template.Library()


def get_user_id(context):
    if context['user'].is_authenticated():
        return context['user'].id
    else:
        return ''


def get_username(context):
    if context['user'].is_authenticated():
        return context['user'].username
    else:
        return ''


register.simple_tag(takes_context=True)(get_user_id)
register.simple_tag(takes_context=True)(get_username)