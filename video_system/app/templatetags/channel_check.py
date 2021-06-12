from django import template
from app.models import Channel


register=template.Library()


@register.filter(name='has_channel')
def has_channel(user):
    try:
        channel=Channel.objects.get(user=user)
    except Channel.DoesNotExist:
        return False
    return True