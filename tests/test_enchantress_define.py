__author__ = 'V8q1ez'

import unittest
import mock

from src.castle.enchantress import enchantress
from src.castle.ccodeparser import CCodeParser
from src.castle.prince import prince
from src.castle.legalist import legalist
from src.castle.ccodeparser import Grammar

class enchantressDefine(unittest.TestCase):
    def setUp(self):
       pass

    def test_define_nominal(self):
        target = enchantress(cinderella=CCodeParser(Grammar()), prince=prince(legalist()))

        inputText = """#define A (5)\n"""
        expectedOutput = """#define A (5)\n"""

        actualOutput = target.formatText( inputText.splitlines() )
        self.assertEqual( expectedOutput.splitlines(), actualOutput )


    @mock.patch.object(legalist, 'handle_macros_name')
    def test_define_lower_case_literal(self, mock_legalist):
        target = enchantress(cinderella=CCodeParser(Grammar()), prince=prince(mock_legalist))
        mock_legalist.handle_macros_name.return_value = 'LITERAL'

        inputText = """#define literal (5)\n"""
        expectedOutput = """#define LITERAL (5)\n"""

        actualOutput = target.formatText( inputText.splitlines() )
        self.assertEqual( expectedOutput.splitlines(), actualOutput )


    @mock.patch.object(legalist, 'handle_macros_name')
    def test_define_lower_case_literal_allowed(self, mock_legalist):
        target = enchantress(cinderella=CCodeParser(Grammar()), prince=prince(mock_legalist))
        mock_legalist.handle_macros_name.return_value = 'literal'

        inputText = """#define literal (5)\n"""
        expectedOutput = """#define literal (5)\n"""

        actualOutput = target.formatText( inputText.splitlines() )
        self.assertEqual( expectedOutput.splitlines(), actualOutput )
