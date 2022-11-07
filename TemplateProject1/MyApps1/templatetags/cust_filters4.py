from django import template
register = template.Library()

def truncate_n(value,n):
    result = value[0:n]
    return result
register.filter('t_n', truncate_n);