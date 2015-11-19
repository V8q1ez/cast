__author__ = 'V8q1ez'

import unittest

from src.castle.ccodeparser import CCodeParser
from src.castle.ccodeparser import Grammar


class CCodeParserMemberAndPointer(unittest.TestCase):
    def setUp(self):
        self._grammar = Grammar()
        self.tkz = CCodeParser(self._grammar)

    def test_member_structure_dereference(self):
        input = []
        input.append('a->b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( Grammar.STRUCTURE_DEREFERENCE, actualOutput[1].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)
        self.assertEqual( Grammar.EOL, actualOutput[3].type)

    def test_member_structure_dereference_with_spaces(self):
        input = []
        input.append('a -> b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( Grammar.STRUCTURE_DEREFERENCE, actualOutput[1].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)
        self.assertEqual( Grammar.EOL, actualOutput[3].type)
