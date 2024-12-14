#!/usr/bin/env python3
"""More involved type annotations"""
from typing import Any, Mapping, Union, TypeVar


typ = TypeVar('T')
Ret = Union[Any, typ]
Def = Union[typ, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Ret:
    """ Return a value from a dict"""
    if key in dct:
        return dct[key]
    else:
        return default
