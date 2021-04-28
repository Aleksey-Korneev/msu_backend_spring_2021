class CustomMeta(type):
    """
    A metaclass which ads 'custom_' to the beginning
    of all class attributes and methods.
    """
    def __new__(cls, name, bases, dct):
        attrs = dict(('custom_' + name, value) for (name, value) \
            in dct.items() if not name.startswith('__'))
        return super(CustomMeta, cls).__new__(cls, name, bases, attrs)
