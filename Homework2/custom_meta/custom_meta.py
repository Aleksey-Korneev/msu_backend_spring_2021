"""Custom metaclass is defined in this module."""


class CustomMeta(type):
    """
    A metaclass which adds 'custom_' to the beginning
    of all class attributes and methods, except magic methods.
    """
    def __new__(cls, name, bases, dct):
        attrs = dict(('custom_' + name, value) for (name, value) in dct.items()
                     if not (name.startswith('__') and name.endswith('__')))
        return super(CustomMeta, cls).__new__(cls, name, bases, attrs)
