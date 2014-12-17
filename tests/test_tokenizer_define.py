__author__ = 'V8q1ez'

import unittest

from src.tokenizer import *


class preprocessorDefine(unittest.TestCase):
    def setUp(self):
       self.tkz = tokenizer()

    def test_define_object_like(self):
        input = []
        input.append('#define a b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)

        self.assertEqual( EOL, actualOutput[3].type)

    def test_define_function_like(self):
        input = []
        input.append('#define a() b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( FUNCTION_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( PARENTHESIS_LEFT, actualOutput[2].type)
        self.assertEqual( PARENTHESIS_RIGHT, actualOutput[3].type)
        self.assertEqual( LITERAL, actualOutput[4].type)
        self.assertEqual( 'b', actualOutput[4].literalValue)

        self.assertEqual( EOL, actualOutput[5].type)

    def test_define_function_like_param(self):
        input = []
        input.append('#define a(x) b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( FUNCTION_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( PARENTHESIS_LEFT, actualOutput[2].type)
        self.assertEqual( LITERAL, actualOutput[3].type)
        self.assertEqual( 'x', actualOutput[3].literalValue)
        self.assertEqual( PARENTHESIS_RIGHT, actualOutput[4].type)
        self.assertEqual( LITERAL, actualOutput[5].type)
        self.assertEqual( 'b', actualOutput[5].literalValue)

        self.assertEqual( EOL, actualOutput[6].type)

    def test_define_function_like_param_2(self):
        input = []
        input.append('#define a(x,y) b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( FUNCTION_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( PARENTHESIS_LEFT, actualOutput[2].type)
        self.assertEqual( LITERAL, actualOutput[3].type)
        self.assertEqual( 'x', actualOutput[3].literalValue)
        self.assertEqual( COMMA, actualOutput[4].type)
        self.assertEqual( LITERAL, actualOutput[5].type)
        self.assertEqual( 'y', actualOutput[5].literalValue)
        self.assertEqual( PARENTHESIS_RIGHT, actualOutput[6].type)
        self.assertEqual( LITERAL, actualOutput[7].type)
        self.assertEqual( 'b', actualOutput[7].literalValue)

        self.assertEqual( EOL, actualOutput[8].type)

    def test_define_function_like_param_2_spaces(self):
        input = []
        input.append('#define a( x , y ) b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( FUNCTION_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( PARENTHESIS_LEFT, actualOutput[2].type)
        self.assertEqual( LITERAL, actualOutput[3].type)
        self.assertEqual( 'x', actualOutput[3].literalValue)
        self.assertEqual( COMMA, actualOutput[4].type)
        self.assertEqual( LITERAL, actualOutput[5].type)
        self.assertEqual( 'y', actualOutput[5].literalValue)
        self.assertEqual( PARENTHESIS_RIGHT, actualOutput[6].type)
        self.assertEqual( LITERAL, actualOutput[7].type)
        self.assertEqual( 'b', actualOutput[7].literalValue)

        self.assertEqual( EOL, actualOutput[8].type)

    def test_define_function_like_param_3(self):
        input = []
        input.append('#define a(x,y,z) b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( FUNCTION_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( PARENTHESIS_LEFT, actualOutput[2].type)
        self.assertEqual( LITERAL, actualOutput[3].type)
        self.assertEqual( 'x', actualOutput[3].literalValue)
        self.assertEqual( COMMA, actualOutput[4].type)
        self.assertEqual( LITERAL, actualOutput[5].type)
        self.assertEqual( 'y', actualOutput[5].literalValue)
        self.assertEqual( COMMA, actualOutput[6].type)
        self.assertEqual( LITERAL, actualOutput[7].type)
        self.assertEqual( 'z', actualOutput[7].literalValue)
        self.assertEqual( PARENTHESIS_RIGHT, actualOutput[8].type)
        self.assertEqual( LITERAL, actualOutput[9].type)
        self.assertEqual( 'b', actualOutput[9].literalValue)

        self.assertEqual( EOL, actualOutput[10].type)

    def test_define_function_like_param_3_spaces(self):
        input = []
        input.append('#define a(  x  ,  y  ,  z  ) b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( FUNCTION_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( PARENTHESIS_LEFT, actualOutput[2].type)
        self.assertEqual( LITERAL, actualOutput[3].type)
        self.assertEqual( 'x', actualOutput[3].literalValue)
        self.assertEqual( COMMA, actualOutput[4].type)
        self.assertEqual( LITERAL, actualOutput[5].type)
        self.assertEqual( 'y', actualOutput[5].literalValue)
        self.assertEqual( COMMA, actualOutput[6].type)
        self.assertEqual( LITERAL, actualOutput[7].type)
        self.assertEqual( 'z', actualOutput[7].literalValue)
        self.assertEqual( PARENTHESIS_RIGHT, actualOutput[8].type)
        self.assertEqual( LITERAL, actualOutput[9].type)
        self.assertEqual( 'b', actualOutput[9].literalValue)

        self.assertEqual( EOL, actualOutput[10].type)

    def test_define_variadic(self):
        input = []
        input.append('#define a(...) b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( FUNCTION_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( PARENTHESIS_LEFT, actualOutput[2].type)
        self.assertEqual( VARIADIC_ARGS, actualOutput[3].type)
        self.assertEqual( PARENTHESIS_RIGHT, actualOutput[4].type)
        self.assertEqual( LITERAL, actualOutput[5].type)
        self.assertEqual( 'b', actualOutput[5].literalValue)

        self.assertEqual( EOL, actualOutput[6].type)

    def test_define_variadic_param_1(self):
        input = []
        input.append('#define a(x,...) b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( FUNCTION_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( PARENTHESIS_LEFT, actualOutput[2].type)
        self.assertEqual( LITERAL, actualOutput[3].type)
        self.assertEqual( 'x', actualOutput[3].literalValue)
        self.assertEqual( COMMA, actualOutput[4].type)
        self.assertEqual( VARIADIC_ARGS, actualOutput[5].type)
        self.assertEqual( PARENTHESIS_RIGHT, actualOutput[6].type)
        self.assertEqual( LITERAL, actualOutput[7].type)
        self.assertEqual( 'b', actualOutput[7].literalValue)

        self.assertEqual( EOL, actualOutput[8].type)

    def test_define_variadic_param_1_spaces(self):
        input = []
        input.append('#define a( x , ... ) b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( FUNCTION_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( PARENTHESIS_LEFT, actualOutput[2].type)
        self.assertEqual( LITERAL, actualOutput[3].type)
        self.assertEqual( 'x', actualOutput[3].literalValue)
        self.assertEqual( COMMA, actualOutput[4].type)
        self.assertEqual( VARIADIC_ARGS, actualOutput[5].type)
        self.assertEqual( PARENTHESIS_RIGHT, actualOutput[6].type)
        self.assertEqual( LITERAL, actualOutput[7].type)
        self.assertEqual( 'b', actualOutput[7].literalValue)

        self.assertEqual( EOL, actualOutput[8].type)

    def test_define_variadic_param_2(self):
        input = []
        input.append('#define a(x,y,...) b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( FUNCTION_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( PARENTHESIS_LEFT, actualOutput[2].type)
        self.assertEqual( LITERAL, actualOutput[3].type)
        self.assertEqual( 'x', actualOutput[3].literalValue)
        self.assertEqual( COMMA, actualOutput[4].type)
        self.assertEqual( LITERAL, actualOutput[5].type)
        self.assertEqual( 'y', actualOutput[5].literalValue)
        self.assertEqual( COMMA, actualOutput[6].type)
        self.assertEqual( VARIADIC_ARGS, actualOutput[7].type)
        self.assertEqual( PARENTHESIS_RIGHT, actualOutput[8].type)
        self.assertEqual( LITERAL, actualOutput[9].type)
        self.assertEqual( 'b', actualOutput[9].literalValue)

        self.assertEqual( EOL, actualOutput[10].type)

    def test_define_variadic_param_2_spaces(self):
        input = []
        input.append('#define a( x , y , ... ) b')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( FUNCTION_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( PARENTHESIS_LEFT, actualOutput[2].type)
        self.assertEqual( LITERAL, actualOutput[3].type)
        self.assertEqual( 'x', actualOutput[3].literalValue)
        self.assertEqual( COMMA, actualOutput[4].type)
        self.assertEqual( LITERAL, actualOutput[5].type)
        self.assertEqual( 'y', actualOutput[5].literalValue)
        self.assertEqual( COMMA, actualOutput[6].type)
        self.assertEqual( VARIADIC_ARGS, actualOutput[7].type)
        self.assertEqual( PARENTHESIS_RIGHT, actualOutput[8].type)
        self.assertEqual( LITERAL, actualOutput[9].type)
        self.assertEqual( 'b', actualOutput[9].literalValue)

        self.assertEqual( EOL, actualOutput[10].type)

    def test_define_object_like_empty_parenthesis_impl(self):
        input = []
        input.append('#define a ()')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( PARENTHESIS_LEFT, actualOutput[2].type)
        self.assertEqual( PARENTHESIS_RIGHT, actualOutput[3].type)

        self.assertEqual( EOL, actualOutput[4].type)

    def test_define_object_like_constant_in_parenthesis(self):
        input = []
        input.append('#define aa (5)')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'aa', actualOutput[1].literalValue)
        self.assertEqual( PARENTHESIS_LEFT, actualOutput[2].type)
        self.assertEqual( LITERAL, actualOutput[3].type)
        self.assertEqual( '5', actualOutput[3].literalValue)
        self.assertEqual( PARENTHESIS_RIGHT, actualOutput[4].type)

        self.assertEqual( EOL, actualOutput[5].type)

    def test_define_object_like_float_constant_in_parenthesis(self):
        input = []
        input.append('#define a (5.5)')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( PARENTHESIS_LEFT, actualOutput[2].type)
        self.assertEqual( LITERAL, actualOutput[3].type)
        self.assertEqual( '5.5', actualOutput[3].literalValue)
        self.assertEqual( PARENTHESIS_RIGHT, actualOutput[4].type)

        self.assertEqual( EOL, actualOutput[5].type)

    def test_define_object_like_string_constant(self):
        input = []
        input.append('#define a "str"')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( QUOTE, actualOutput[2].type)
        self.assertEqual( STRING, actualOutput[3].type)
        self.assertEqual( 'str', actualOutput[3].literalValue)
        self.assertEqual( QUOTE, actualOutput[4].type)

        self.assertEqual( EOL, actualOutput[5].type)

    def test_define_object_like_str_const_like_variadic(self):
        input = []
        input.append('#define a "..."')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( QUOTE, actualOutput[2].type)
        self.assertEqual( STRING, actualOutput[3].type)
        self.assertEqual( '...', actualOutput[3].literalValue)
        self.assertEqual( QUOTE, actualOutput[4].type)

        self.assertEqual( EOL, actualOutput[5].type)

    def test_define_function_like_sum(self):
        input = []
        input.append('#define sum(x,y) (x)+(y)')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( FUNCTION_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'sum', actualOutput[1].literalValue)
        self.assertEqual( PARENTHESIS_LEFT, actualOutput[2].type)
        self.assertEqual( LITERAL, actualOutput[3].type)
        self.assertEqual( 'x', actualOutput[3].literalValue)
        self.assertEqual( COMMA, actualOutput[4].type)
        self.assertEqual( LITERAL, actualOutput[5].type)
        self.assertEqual( 'y', actualOutput[5].literalValue)
        self.assertEqual( PARENTHESIS_RIGHT, actualOutput[6].type)
        self.assertEqual( PARENTHESIS_LEFT, actualOutput[7].type)
        self.assertEqual( LITERAL, actualOutput[8].type)
        self.assertEqual( 'x', actualOutput[8].literalValue)
        self.assertEqual( PARENTHESIS_RIGHT, actualOutput[9].type)
        self.assertEqual( LITERAL, actualOutput[10].type)
        self.assertEqual( '+', actualOutput[10].literalValue)
        self.assertEqual( PARENTHESIS_LEFT, actualOutput[11].type)
        self.assertEqual( LITERAL, actualOutput[12].type)
        self.assertEqual( 'y', actualOutput[12].literalValue)
        self.assertEqual( PARENTHESIS_RIGHT, actualOutput[13].type)

        self.assertEqual( EOL, actualOutput[14].type)

    def test_define_function_like_sum_spaces(self):
        input = []
        input.append('#define sum( x , y ) ( x ) + ( y )')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( FUNCTION_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'sum', actualOutput[1].literalValue)
        self.assertEqual( PARENTHESIS_LEFT, actualOutput[2].type)
        self.assertEqual( LITERAL, actualOutput[3].type)
        self.assertEqual( 'x', actualOutput[3].literalValue)
        self.assertEqual( COMMA, actualOutput[4].type)
        self.assertEqual( LITERAL, actualOutput[5].type)
        self.assertEqual( 'y', actualOutput[5].literalValue)
        self.assertEqual( PARENTHESIS_RIGHT, actualOutput[6].type)
        self.assertEqual( PARENTHESIS_LEFT, actualOutput[7].type)
        self.assertEqual( LITERAL, actualOutput[8].type)
        self.assertEqual( 'x', actualOutput[8].literalValue)
        self.assertEqual( PARENTHESIS_RIGHT, actualOutput[9].type)
        self.assertEqual( LITERAL, actualOutput[10].type)
        self.assertEqual( '+', actualOutput[10].literalValue)
        self.assertEqual( PARENTHESIS_LEFT, actualOutput[11].type)
        self.assertEqual( LITERAL, actualOutput[12].type)
        self.assertEqual( 'y', actualOutput[12].literalValue)
        self.assertEqual( PARENTHESIS_RIGHT, actualOutput[13].type)

        self.assertEqual( EOL, actualOutput[14].type)

    def test_define_wrong_function_like_sum(self):
        input = []
        input.append('#define sum (x,y) (x)+(y)')

        actualOutput = self.tkz.parseText(input)

        self.assertEqual( OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'sum', actualOutput[1].literalValue)
        self.assertEqual( PARENTHESIS_LEFT, actualOutput[2].type)
        self.assertEqual( LITERAL, actualOutput[3].type)
        self.assertEqual( 'x', actualOutput[3].literalValue)
        self.assertEqual( COMMA, actualOutput[4].type)
        self.assertEqual( LITERAL, actualOutput[5].type)
        self.assertEqual( 'y', actualOutput[5].literalValue)
        self.assertEqual( PARENTHESIS_RIGHT, actualOutput[6].type)
        self.assertEqual( PARENTHESIS_LEFT, actualOutput[7].type)
        self.assertEqual( LITERAL, actualOutput[8].type)
        self.assertEqual( 'x', actualOutput[8].literalValue)
        self.assertEqual( PARENTHESIS_RIGHT, actualOutput[9].type)
        self.assertEqual( LITERAL, actualOutput[10].type)
        self.assertEqual( '+', actualOutput[10].literalValue)
        self.assertEqual( PARENTHESIS_LEFT, actualOutput[11].type)
        self.assertEqual( LITERAL, actualOutput[12].type)
        self.assertEqual( 'y', actualOutput[12].literalValue)
        self.assertEqual( PARENTHESIS_RIGHT, actualOutput[13].type)

        self.assertEqual( EOL, actualOutput[14].type)
