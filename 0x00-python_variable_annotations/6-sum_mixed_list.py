#!/usr/bin/env python3
"""Module that contains sum_mixed_list function which takes a list mxd_lst of 
integers and floats and returns their sum as a float
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns the sum of list items"""
    return sum(mxd_lst)
