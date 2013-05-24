from functools import partial, wraps
from itertools import ifilter, imap
from operator import not_


def list_subtract(a, b):
    """Return a list ``a`` without the elements of ``b``.

    If a particular value is in ``a`` twice and ``b`` once then the returned
    list then that value will appear once in the returned list.
    """
    a_only = list(a)
    for x in b:
        if x in a_only:
            a_only.remove(x)
    return a_only


def identity(x):
    return x


def caller(method_name, *args, **kwargs):
    def call_obj(obj):
        return getattr(obj, method_name)(*args, **kwargs)
    return call_obj


def compose(*functions):
    if not functions:
        raise ValueError("Must specify functions to compose")
    def composed(*args, **kwargs):
        fs = list(functions)
        y = fs.pop()(*args, **kwargs)
        while fs:
            f = fs.pop()
            y = f(y)
        return y
    return composed


def wrap_result(wrapper):
    return lambda f: wraps(f)(compose(wrapper, f))


negate = wrap_result(not_)


def on_items(f, d):
    return compose(dict, f, caller('items'))(d)


def dichotomy(p, xs):
    return ifilter(negate(p), xs), ifilter(p, xs)


def map_dict(f, d):
    return on_items(partial(imap, f), d)


def filter_dict(p, d):
    return on_items(partial(ifilter, p), d)


def map_keys(f, d):
    return map_dict(lambda (k, v): (f(k), v), d)


def filter_keys(f, d):
    return filter_dict(lambda (k, v): f(k), d)


def map_values(f, d):
    """Map ``f`` across the values of ``d``.

    :return: A dict with the same keys as ``d``, where the value
        of each key ``k`` is ``f(d[k])``.
    """
    return map_dict(lambda (k, v): (k, f(v)), d)


def filter_values(f, d):
    """Filter ``dictionary`` by its values using ``function``."""
    return filter_dict(lambda (k, v): f(v), d)


def dict_subtract(a, b):
    """Return the part of ``a`` that's not in ``b``."""
    return dict((k, a[k]) for k in set(a) - set(b))
