#!/usr/bin/env python3
"""Module that contains sum_list which takes a list input_list of floats
as argument and returns their sum as a float
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """takes input_list as argument and returns the sum of its items
    """
    return sum(input_list)
