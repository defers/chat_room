
def get_class_representation(_class):
    dict_attrs = _class.__dict__
    text_attrs = [f"{key}:{dict_attrs.get(key)}" for key in dict_attrs.keys()]
    return _class.__class__.__name__ + " " + str(text_attrs)

