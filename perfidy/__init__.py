__all__ = [
    'caller',
    'compose',
    'dichotomy',
    'dict_subtract',
    'filter_dict',
    'filter_keys',
    'filter_values',
    'frozendict',
    'identity',
    'list_subtract',
    'map_dict',
    'map_keys',
    'map_values',
    'on_items',
    'wrap_result',
    'safe_hasattr',
    'try_import',
    'try_imports',
    ]

from ._dict import frozendict
from ._extras import (
    safe_hasattr,
    try_import,
    try_imports,
    )
from ._func import (
    caller,
    compose,
    dichotomy,
    dict_subtract,
    filter_dict,
    filter_keys,
    filter_values,
    identity,
    list_subtract,
    map_dict,
    map_keys,
    map_values,
    on_items,
    wrap_result,
    )


# same format as sys.version_info: "A tuple containing the five components of
# the version number: major, minor, micro, releaselevel, and serial. All
# values except releaselevel are integers; the release level is 'alpha',
# 'beta', 'candidate', or 'final'. The version_info value corresponding to the
# Python version 2.0 is (2, 0, 0, 'final', 0)."  Additionally we use a
# releaselevel of 'dev' for unreleased under-development code.
#
# If the releaselevel is 'alpha' then the major/minor/micro components are not
# established at this point, and setup.py will use a version of next-$(revno).
# If the releaselevel is 'final', then the tarball will be major.minor.micro.
# Otherwise it is major.minor.micro~$(revno).

__version__ = (0, 0, 2, 'final', 0)
