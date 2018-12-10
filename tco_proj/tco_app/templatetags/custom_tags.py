# https://www.codementor.io/hiteshgarg14/
# creating-custom-template-tags-in-django-application-58wvmqm5f
from django import template

register = template.Library()

# simple_tag: Processes the data and returns a string
# inclusion_tag: Processes the data and returns a rendered template
# assignment_tag: Processes the data and sets a variable in the context

from ..models import SystemTable

@register.simple_tag
def system_count():
    return SystemTable.objects.count()

@register.inclusion_tag("../templates/tco_app/s.html")
def system_to_html():
    systems = SystemTable.objects.all()
    return {'systems': systems}

# # https://stackoverflow.com/questions/21021690/python-django-custom-template-tags-register-assignment-tag-not-working
# # Django 1.4 added the assignment_tag helper to ease the creation of template tags that store results 
# # in a template variable. The simple_tag() helper has gained this same ability, making the  
# # assignment_tag obsolete. Tags that use assignment_tag should be updated to use simple_tag.
# @register.assignment_tag 
# def systems_by_assignment(id_s=2):
#     s = SystemTable.objects.filter(id=id_s)