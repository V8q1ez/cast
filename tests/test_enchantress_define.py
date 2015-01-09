__author__ = 'V8q1ez'

import unittest

from src.castle.enchantress import *


class enchantressDefine(unittest.TestCase):
    def setUp(self):
       self.target = enchantress()

    def test_define_nominal(self):
        inputText = """#define A (5)\n"""
        expectedOutput = """#define A (5)\n"""

        actualOutput = self.target.formatText( inputText.splitlines() )

        self.assertEqual( expectedOutput.splitlines(), actualOutput )

    def test_define_lower_case_literal(self):
        inputText = """#define literal (5)\n"""
        expectedOutput = """#define LITERAL (5)\n"""

        actualOutput = self.target.formatText( inputText.splitlines() )

        self.assertEqual( expectedOutput.splitlines(), actualOutput )
