from django import template

register = template.Library()

@register.filter
def get_item(array, index):
    try:
        return array[index]
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
