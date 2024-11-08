import requests
from inspect import getmodule
def intro_info(obj):
    dict_obj = {}
    dict_obj['type'] = type(obj)
    dict_obj['attributes'] = [i for i in dir(obj) if not i.startswith('__')]
    dict_obj['methods'] = [i for i in dir(obj) if i.startswith('__')]
    dict_obj['module'] = getmodule(obj)
    dict_obj['identifier'] = id(obj)

    return dict_obj


number_info = intro_info(42)
print(number_info)

string_info = intro_info('somthing word')
print(string_info)