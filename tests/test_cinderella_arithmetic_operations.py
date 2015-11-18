__author__ = 'V8q1ez'

import unittest

from src.castle.cinderella import *


class compilerArithmeticOperations(unittest.TestCase):
    def setUp(self):
        self._grammar = Grammar()
        self.tkz = cinderella(self._grammar)

    def test_arithmetic_assignment(self):
        input = []
        input.append('a=b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( Grammar.ASSIGNMENT, actualOutput[1].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[3].type)

    def test_arithmetic_addition(self):
        input = []
        input.append('a+b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( Grammar.ADDITION, actualOutput[1].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[3].type)

    def test_arithmetic_addition_with_spaces(self):
        input = []
        input.append('a + b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( Grammar.ADDITION, actualOutput[1].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[3].type)

    def test_arithmetic_subtraction(self):
        input = []
        input.append('a-b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( Grammar.SUBTRACTION, actualOutput[1].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[3].type)

    def test_arithmetic_subtraction_with_spaces(self):
        input = []
        input.append('a - b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( Grammar.SUBTRACTION, actualOutput[1].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[3].type)

    def test_arithmetic_pre_increment(self):
        input = []
        input.append('++a')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.INCREMENT, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[2].type)

    def test_arithmetic_two_pre_increments(self):
        input = []
        input.append('++a,++b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.INCREMENT, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( Grammar.COMMA, actualOutput[2].type)
        self.assertEqual( Grammar.INCREMENT, actualOutput[3].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[4].type)
        self.assertEqual( 'b', actualOutput[4].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[5].type)

    def test_arithmetic_post_increment(self):
        input = []
        input.append('a++')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( Grammar.INCREMENT, actualOutput[1].type)

        self.assertEqual( Grammar.EOL, actualOutput[2].type)

    def test_arithmetic_two_post_increments(self):
        input = []
        input.append('a++,b++')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( Grammar.INCREMENT, actualOutput[1].type)
        self.assertEqual( Grammar.COMMA, actualOutput[2].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[3].type)
        self.assertEqual( 'b', actualOutput[3].literalValue)
        self.assertEqual( Grammar.INCREMENT, actualOutput[4].type)

        self.assertEqual( Grammar.EOL, actualOutput[5].type)

    def test_arithmetic_pre_decrement(self):
        input = []
        input.append('--a')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.DECREMENT, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[2].type)

    def test_arithmetic_two_pre_decrements(self):
        input = []
        input.append('--a,--b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.DECREMENT, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( Grammar.COMMA, actualOutput[2].type)
        self.assertEqual( Grammar.DECREMENT, actualOutput[3].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[4].type)
        self.assertEqual( 'b', actualOutput[4].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[5].type)

    def test_arithmetic_post_decrement(self):
        input = []
        input.append('a--')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( Grammar.DECREMENT, actualOutput[1].type)

        self.assertEqual( Grammar.EOL, actualOutput[2].type)

    def test_arithmetic_two_post_decrements(self):
        input = []
        input.append('a--,b--')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( Grammar.DECREMENT, actualOutput[1].type)
        self.assertEqual( Grammar.COMMA, actualOutput[2].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[3].type)
        self.assertEqual( 'b', actualOutput[3].literalValue)
        self.assertEqual( Grammar.DECREMENT, actualOutput[4].type)

        self.assertEqual( Grammar.EOL, actualOutput[5].type)

    def test_pre_inc_with_unary_plus(self):
        input = []
        input.append('+++a')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.INCREMENT, actualOutput[0].type)
        self.assertEqual( Grammar.ADDITION, actualOutput[1].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[2].type)
        self.assertEqual( 'a', actualOutput[2].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[3].type)

    def test_pre_dec_with_unary_minus(self):
        input = []
        input.append('---a')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.DECREMENT, actualOutput[0].type)
        self.assertEqual( Grammar.SUBTRACTION, actualOutput[1].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[2].type)
        self.assertEqual( 'a', actualOutput[2].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[3].type)

    def test_pre_inc_with_unary_plus_spaces(self):
        input = []
        input.append('++ + a')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.INCREMENT, actualOutput[0].type)
        self.assertEqual( Grammar.ADDITION, actualOutput[1].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[2].type)
        self.assertEqual( 'a', actualOutput[2].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[3].type)

    def test_pre_dec_with_unary_minus_spaces(self):
        input = []
        input.append('-- - a')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.DECREMENT, actualOutput[0].type)
        self.assertEqual( Grammar.SUBTRACTION, actualOutput[1].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[2].type)
        self.assertEqual( 'a', actualOutput[2].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[3].type)

    def test_arithmetic_division(self):
        input = []
        input.append('a/b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( Grammar.DIVISION, actualOutput[1].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[3].type)

    def test_arithmetic_division_with_spaces(self):
        input = []
        input.append('a / b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( Grammar.DIVISION, actualOutput[1].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[3].type)

    def test_arithmetic_modulo(self):
        input = []
        input.append('a%b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( Grammar.MODULO, actualOutput[1].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[3].type)

    def test_arithmetic_modulo_with_spaces(self):
        input = []
        input.append('a % b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( Grammar.LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( Grammar.MODULO, actualOutput[1].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[3].type)
