"""Custom metaclass is defined in this module."""


class CustomMeta(type):
    """
    A metaclass which adds 'custom_' to the beginning
    of all class attributes and methods, except magic methods.
    """

    def __new__(cls, name, bases, attrs):
        custom_attrs = {
            key
            if key.startswith("__") and key.endswith("__")
            else f"custom_{key}": value
            for key, value in attrs.items()
        }
        custom_name = f"custom_{name}"
        cls.custom_attrs = custom_attrs
        return super().__new__(cls, custom_name, bases, custom_attrs)

    def __call__(cls, *args, **kwargs):
        res = super(CustomMeta, cls).__call__(*args, **kwargs)
        attrs = dir(res)
        for attr in attrs:
            if not (
                attr.startswith("__")
                and attr.endswith("__")
                or attr in cls.custom_attrs
            ):
                value = getattr(res, attr)

                delattr(res, attr)
                setattr(res, f"custom_{attr}", value)

        return res
