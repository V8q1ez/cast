__author__ = 'V8q1ez'

import unittest

from src.tokenizer import *


class preprocessorDefine(unittest.TestCase):
    def setUp(self):
       self.tkz = tokenizer()

    def test_define_object_like(self):
        input = '#define a b'

        actualOutput = self.tkz.parseString(input)

        self.assertEqual( OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)

    def test_define_function_like(self):
        input = '#define a() b'

        actualOutput = self.tkz.parseString(input)

        self.assertEqual( FUNCTION_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( PARENTHESIS_LEFT, actualOutput[2].type)
        self.assertEqual( PARENTHESIS_RIGHT, actualOutput[3].type)
        self.assertEqual( LITERAL, actualOutput[4].type)
        self.assertEqual( 'b', actualOutput[4].literalValue)

    def test_define_function_like_param(self):
        input = '#define a(x) b'

        actualOutput = self.tkz.parseString(input)

        self.assertEqual( FUNCTION_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( PARENTHESIS_LEFT, actualOutput[2].type)
        self.assertEqual( LITERAL, actualOutput[3].type)
        self.assertEqual( 'x', actualOutput[3].literalValue)
        self.assertEqual( PARENTHESIS_RIGHT, actualOutput[4].type)
        self.assertEqual( LITERAL, actualOutput[5].type)
        self.assertEqual( 'b', actualOutput[5].literalValue)

    def test_define_function_like_param_2(self):
        input = '#define a(x,y) b'

        actualOutput = self.tkz.parseString(input)

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

    def test_define_function_like_param_2_spaces(self):
        input = '#define a( x , y ) b'

        actualOutput = self.tkz.parseString(input)

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

    def test_define_function_like_param_3(self):
        input = '#define a(x,y,z) b'

        actualOutput = self.tkz.parseString(input)

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

    def test_define_function_like_param_3_spaces(self):
        input = '#define a(  x  ,  y  ,  z  ) b'

        actualOutput = self.tkz.parseString(input)

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

    def test_define_variadic(self):
        input = '#define a(...) b'

        actualOutput = self.tkz.parseString(input)

        self.assertEqual( FUNCTION_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( PARENTHESIS_LEFT, actualOutput[2].type)
        self.assertEqual( VARIADIC_ARGS, actualOutput[3].type)
        self.assertEqual( PARENTHESIS_RIGHT, actualOutput[4].type)
        self.assertEqual( LITERAL, actualOutput[5].type)
        self.assertEqual( 'b', actualOutput[5].literalValue)

    def test_define_variadic_param_1(self):
        input = '#define a(x,...) b'

        actualOutput = self.tkz.parseString(input)

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

    def test_define_variadic_param_1_spaces(self):
        input = '#define a( x , ... ) b'

        actualOutput = self.tkz.parseString(input)

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

    def test_define_variadic_param_2(self):
        input = '#define a(x,y,...) b'

        actualOutput = self.tkz.parseString(input)

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

    def test_define_variadic_param_2_spaces(self):
        input = '#define a( x , y , ... ) b'

        actualOutput = self.tkz.parseString(input)

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

    def test_define_object_like_empty_parenthesis_impl(self):
        input = '#define a ()'

        actualOutput = self.tkz.parseString(input)

        self.assertEqual( OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( PARENTHESIS_LEFT, actualOutput[2].type)
        self.assertEqual( PARENTHESIS_RIGHT, actualOutput[3].type)

    def test_define_object_like_constant_in_parenthesis(self):
        input = '#define aa (5)'

        actualOutput = self.tkz.parseString(input)

        self.assertEqual( OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'aa', actualOutput[1].literalValue)
        self.assertEqual( PARENTHESIS_LEFT, actualOutput[2].type)
        self.assertEqual( LITERAL, actualOutput[3].type)
        self.assertEqual( '5', actualOutput[3].literalValue)
        self.assertEqual( PARENTHESIS_RIGHT, actualOutput[4].type)

    def test_define_object_like_float_constant_in_parenthesis(self):
        input = '#define a (5.5)'

        actualOutput = self.tkz.parseString(input)

        self.assertEqual( OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( PARENTHESIS_LEFT, actualOutput[2].type)
        self.assertEqual( LITERAL, actualOutput[3].type)
        self.assertEqual( '5.5', actualOutput[3].literalValue)
        self.assertEqual( PARENTHESIS_RIGHT, actualOutput[4].type)

    def test_define_function_like_sum(self):
        input = '#define sum(x,y) (x)+(y)'

        actualOutput = self.tkz.parseString(input)

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

    def test_define_function_like_sum_spaces(self):
        input = '#define sum( x , y ) ( x ) + ( y )'

        actualOutput = self.tkz.parseString(input)

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

    def test_define_wrong_function_like_sum(self):
        input = '#define sum (x,y) (x)+(y)'

        actualOutput = self.tkz.parseString(input)

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
