from django import template
from django.db.models.query import QuerySet

register = template.Library()

@register.filter
def get_item(array:dict, index):
    try:
        return array.get(index)
    except IndexError:
        return None
    
@register.filter
def get_dict_item(dictionary:dict, key):
    return dictionary.get(key)

@register.filter
def get_item_2arr(array:dict, index, index2):
    try:
        return array[index][index2]
    except (IndexError, TypeError):
        return None
     
    
@register.filter
def url_slicer(url:list[str], delimeter:str):
    try:
        new_url = '/'.join(url).split(delimeter)
        return new_url[0] + delimeter
    except IndexError:
        return None
    
@register.filter(name='split')
def split(value, key): 
    value.split("key")
    return value.split(key)


@register.filter(name='queryset_get')
def queryset_get(queryset, user_id):
    try:
        record = queryset.filter(student=user_id).first()  # Get the first result if it exists
        if record:
            return record
        return None
    except Exception as e:
        return None
