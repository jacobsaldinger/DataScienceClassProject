#!/usr/bin/env python3
"""
Unit and regression test for the analyze_reactions package.
"""

# Import package, test suite, and other packages as needed
import sys
import unittest
from contextlib import contextmanager
from io import StringIO
import os
from analyze_reactions.rxncount import main

from analyze_reactions import main


class TestMain(unittest.TestCase):
    CURRENT_DIR = os.path.dirname(__file__)
    MAIN_DIR = os.path.join(CURRENT_DIR, '..')
    PROJ_DIR = os.path.join(MAIN_DIR, 'analyze_reactions')
    DATA_DIR = os.path.join(PROJ_DIR, 'data')
    SAMPLE_DATA_FILE_LOC = os.path.join(DATA_DIR, 'test.txt')
    #Test all arguments are output as a tuple
    def testallArgs(self):
        test_input=["-txtfile",self.SAMPLE_DATA_FILE_LOC]
        desiredoutput=main(test_input)
        with capture_stdout(main, test_input) as output:
            self.assertEqual(desiredoutput,(2,2,4))
    #Test all arguments are output as a tuple
    def testForwardArgs(self):
        test_input=["-txtfile",self.SAMPLE_DATA_FILE_LOC,'-f']
        desiredoutput=main(test_input)
        with capture_stdout(main, test_input) as output:
            self.assertEqual(desiredoutput,(2,None,None))

# Utility functions

# From http://schinckel.net/2013/04/15/capture-and-test-sys.stdout-sys.stderr-in-unittest.testcase/
@contextmanager
def capture_stdout(command, *args, **kwargs):
    # pycharm doesn't know six very well, so ignore the false warning
    # noinspection PyCallingNonCallable
    out, sys.stdout = sys.stdout, StringIO()
    command(*args, **kwargs)
    sys.stdout.seek(0)
    yield sys.stdout.read()
    sys.stdout = out
