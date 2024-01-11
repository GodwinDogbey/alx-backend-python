#!/usr/bin/env python3
""" Basic annotations  - mixed list"""

from typing import Union, List


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """ Returns the sum of all elements of a list """
    return sum(mxd_list)
