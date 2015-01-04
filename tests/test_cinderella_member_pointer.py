__author__ = 'V8q1ez'

import unittest

from src.castle.cinderella import *


class compilerMemberAndPointer(unittest.TestCase):
    def setUp(self):
       self.tkz = cinderella()

    def test_member_structure_dereference(self):
        input = []
        input.append('a->b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( STRUCTURE_DEREFERENCE, actualOutput[1].type)
        self.assertEqual( LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)
        self.assertEqual( EOL, actualOutput[3].type)

    def test_member_structure_dereference_with_spaces(self):
        input = []
        input.append('a -> b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( STRUCTURE_DEREFERENCE, actualOutput[1].type)
        self.assertEqual( LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)
        self.assertEqual( EOL, actualOutput[3].type)
