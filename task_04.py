#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Litterboxes and catfood for the  kittens"""


def too_many_kittens(kittens, litterboxes, catfood):
    """Ensures at least one litterbox for each kitten and some catfood.


    Args:
        kittens (int):  Arg to be compared to the number of litterboxes.
        litterboxes (int):  Arg to be compared agains kittens and catfood.
        catfood (boolean):  Arg to be compared to the number of litterboxes.


    Returns:
        Boolean:   True or False


    Examples:


        >>> too_many_kittens(13, 12, True)
        True
        >>> too_many_kittens(12, 12, False)
        True
    """

    return not (litterboxes >= kittens and catfood)
