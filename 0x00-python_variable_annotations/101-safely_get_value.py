#!/usr/bin/env python3
"""Task 11 module.
"""

from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Union[T, None] = None
) -> Union[Any, T]:
    """Adding type annotations to the function.
    """
    if key in dct:
        return dct[key]
    else:
        return default
