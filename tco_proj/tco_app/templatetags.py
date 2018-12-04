from .models import SystemTable
from django import template

register = template.Library()

@register.inclusion_tag("simulation.html")
def system_select():
    system_list = SystemTable.objects.all()
    return {'systems' : system_list}