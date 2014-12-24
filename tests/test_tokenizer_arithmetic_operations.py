__author__ = 'V8q1ez'

import unittest

from src.tokenizer import *


class compilerArithmeticOperations(unittest.TestCase):
    def setUp(self):
       self.tkz = tokenizer()

    def test_arithmetic_assignment(self):
        input = []
        input.append('a=b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( ASSIGNMENT, actualOutput[1].type)
        self.assertEqual( LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)

        self.assertEqual( EOL, actualOutput[3].type)

    def test_arithmetic_addition(self):
        input = []
        input.append('a+b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( ADDITION, actualOutput[1].type)
        self.assertEqual( LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)

        self.assertEqual( EOL, actualOutput[3].type)

    def test_arithmetic_addition_with_spaces(self):
        input = []
        input.append('a + b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( ADDITION, actualOutput[1].type)
        self.assertEqual( LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)

        self.assertEqual( EOL, actualOutput[3].type)

    def test_arithmetic_subtraction(self):
        input = []
        input.append('a-b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( SUBTRACTION, actualOutput[1].type)
        self.assertEqual( LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)

        self.assertEqual( EOL, actualOutput[3].type)

    def test_arithmetic_subtraction_with_spaces(self):
        input = []
        input.append('a - b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( SUBTRACTION, actualOutput[1].type)
        self.assertEqual( LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)

        self.assertEqual( EOL, actualOutput[3].type)

    def test_arithmetic_pre_increment(self):
        input = []
        input.append('++a')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( INCREMENT, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)

        self.assertEqual( EOL, actualOutput[2].type)

    def test_arithmetic_two_pre_increments(self):
        input = []
        input.append('++a,++b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( INCREMENT, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( COMMA, actualOutput[2].type)
        self.assertEqual( INCREMENT, actualOutput[3].type)
        self.assertEqual( LITERAL, actualOutput[4].type)
        self.assertEqual( 'b', actualOutput[4].literalValue)

        self.assertEqual( EOL, actualOutput[5].type)

    def test_arithmetic_post_increment(self):
        input = []
        input.append('a++')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( INCREMENT, actualOutput[1].type)

        self.assertEqual( EOL, actualOutput[2].type)

    def test_arithmetic_two_post_increments(self):
        input = []
        input.append('a++,b++')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( INCREMENT, actualOutput[1].type)
        self.assertEqual( COMMA, actualOutput[2].type)
        self.assertEqual( LITERAL, actualOutput[3].type)
        self.assertEqual( 'b', actualOutput[3].literalValue)
        self.assertEqual( INCREMENT, actualOutput[4].type)

        self.assertEqual( EOL, actualOutput[5].type)

    def test_arithmetic_pre_decrement(self):
        input = []
        input.append('--a')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( DECREMENT, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)

        self.assertEqual( EOL, actualOutput[2].type)

    def test_arithmetic_two_pre_decrements(self):
        input = []
        input.append('--a,--b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( DECREMENT, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( COMMA, actualOutput[2].type)
        self.assertEqual( DECREMENT, actualOutput[3].type)
        self.assertEqual( LITERAL, actualOutput[4].type)
        self.assertEqual( 'b', actualOutput[4].literalValue)

        self.assertEqual( EOL, actualOutput[5].type)

    def test_arithmetic_post_decrement(self):
        input = []
        input.append('a--')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( DECREMENT, actualOutput[1].type)

        self.assertEqual( EOL, actualOutput[2].type)

    def test_arithmetic_two_post_decrements(self):
        input = []
        input.append('a--,b--')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( LITERAL, actualOutput[0].type)
        self.assertEqual( 'a', actualOutput[0].literalValue)
        self.assertEqual( DECREMENT, actualOutput[1].type)
        self.assertEqual( COMMA, actualOutput[2].type)
        self.assertEqual( LITERAL, actualOutput[3].type)
        self.assertEqual( 'b', actualOutput[3].literalValue)
        self.assertEqual( DECREMENT, actualOutput[4].type)

        self.assertEqual( EOL, actualOutput[5].type)
