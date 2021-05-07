#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 22:59:10 2016

@author: Theo
"""
myModules = '/Users/Theo/GRWMODELS/Python_projects/mfpy/modules'

import sys

if not myModules in sys.path:
    sys.path.insert(0, myModules)

import test_mfgrid
import test_mfpath0
import test_mfpath1
import test_mfpath2
import test_mfpath3
import test_fdm3

import unittest

#loadTests = unittest.defaultTestLoader.loadTestsFromTestCase
runTests =  unittest.TextTestRunner
loadAllTests = unittest.defaultTestLoader.loadTestsFromNames


names = ['test_mfgrid.MfgridTests',
         'test_mfpath0.Mfpath1dConstantVelocityTests',
         'test_mfpath1.Mfpath1dVariableVelocityTests',
         'test_mfpath2.MfpathAxialFlowTests',
         'test_mfpath3.MfpathRadialFlowTests',
         'test_fdm3.Fdm3Tests']

suite = loadAllTests(names)

runTests(verbosity=2).run(suite)
