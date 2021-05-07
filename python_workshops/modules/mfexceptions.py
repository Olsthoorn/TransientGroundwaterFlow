# -*- coding: utf-8 -*-
"""mfLab exception classes.

Created on Fri Sep 30 04:12:02 2016

@author: Theo
"""

class InputError(Exception):
    """Exception raised for errors in the input.
    """
    pass
    #def __init__(self, expression, message):
    #    self.expression = expression
    #    self.message = message

class ShapeError(Exception):
    """Exception raised then shapes don't match.
    """
    pass
    #def __init__(self, expression, message):
    #    self.expression = expression
    #    self.message = message
