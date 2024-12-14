#!/usr/bin/env python3
"""functions"""
from typing import Callable, Iterator, Union, Optional, List, Tuple


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    return a function that multiplies a float by multiplier.
    """
    def fl(n: float) -> float:
        """ multiplies a float by multiplier """
        return float(n * multiplier)

    return fl
