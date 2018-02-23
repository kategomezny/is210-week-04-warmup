#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module does some pretty crazy math.

   Calls a function and assigns the result to a global variable.


    Calls the function: 
    crazy_math(monkeys, hours, typewriters=None, bananas=None):
    stored in the file hamlet.py


    Returns:
        Assigns the returned result to a new global variable named POSITIONAL.

        
    Examples:

    
       >>> import task_02
       >>> print task_02.POSITIONAL
       0.00374391674995
    """

import hamlet

POSITIONAL = hamlet.crazy_math(4, 100000, 8, 98)



