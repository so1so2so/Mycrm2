#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def render_app_name(admin_class):
    return admin_class.model._meta.verbose_name

@register.simple_tag
def get_query_sets(admin_class):
    return admin_class.model.objects.all()

@register.simple_tag
def build_table_row(obj, admin_class):
    row_ele = ""
    for column in admin_class.list_display:
        field_obj = obj._meta.get_field(column)
        if field_obj.choices:  # choices type
            column_data = getattr(obj, "get_%s_display" % column)()
        else:
            column_data = getattr(obj, column)

        if type(column_data).__name__ == 'datetime':
            column_data = column_data.strftime("%Y-%m-%d %H:%M:%S")

        row_ele += "<td>%s</td>" % column_data

    return mark_safe(row_ele)