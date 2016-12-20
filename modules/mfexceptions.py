# -*- coding: utf-8 -*-
"""mfLab exception classes.

Created on Fri Sep 30 04:12:02 2016

@author: Theo
"""

class InputError(BaseException):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """
    pass
    #def __init__(self, expression, message):
    #    self.expression = expression
    #    self.message = message
