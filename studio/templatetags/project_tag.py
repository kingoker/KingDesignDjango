from django import template

from ..models import Project

register = template.Library()


@register.inclusion_tag('studio/banner.html')
def get_last_project():
    project = Project.objects.order_by("-id")[:1]
    return {"last_project": project}
