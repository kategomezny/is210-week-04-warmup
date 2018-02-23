#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""


def know_what_i_mean(wink, numwink=2):
    """Returns the number of times that you mean.
    
    
    Args:
        wink(str):  Arg to be multiplied by numwik.
        numwink(int):  Arg to multiply wink.
        
        
    Returns:
        str:  'Know what I mean?' plus wink multiplied by
        numwink, plus nudges multiplied by numwink.
        
        
    Examples:
    
        >>>know_what_i_mean('kt', 4)
        'Know what I mean? ktktktkt, nudge nudge nudge nudge'
        
        >>> know_what_i_mean('a')
        'Know what I mean? aa, nudge nudge'
    """

    winks = (wink * numwink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean? {}, {}'.format(winks, nudges)
    return retstr
