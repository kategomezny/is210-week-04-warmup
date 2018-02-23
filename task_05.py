#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Logical comparison between two parameters"""


def defaults(my_required, my_optional=True):
    """Compares two parameters, returns boolean.

    Args:
        my_required (boolean):  Arg to be compared to my_optional.
        my_optional (boolean, optional): Arg to be compared to my_required.

    Returns:
        Boolean:  True or False.

    Examples:

        >>> defaults(True)
        True

        >>> defaults(True, False)
        False
    """
    
    if my_required == my_optional:
        return True
    else:
        return False
