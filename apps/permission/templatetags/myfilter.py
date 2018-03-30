# -*- coding:utf-8 -*-

from django import template

register = template.Library()

@register.filter
def get_key(d, key_name):
    return d.get(key_name)