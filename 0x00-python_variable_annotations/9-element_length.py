#!/usr/bin/env python3
"""
Duck type iterable object
"""
from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Annotate function param
    """
    return [(i, len(i)) for i in lst]
