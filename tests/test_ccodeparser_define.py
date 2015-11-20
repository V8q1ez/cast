__author__ = 'V8q1ez'

import unittest

from src.castle.ccodeparser import CCodeParser
from src.castle.ccodeparser import Grammar
from src.castle.ccodeparser import CCodeParsingContext


class CCodeParserDefine(unittest.TestCase):
    def setUp(self):
        self._grammar = Grammar()
        self.tkz = CCodeParser(self._grammar)

    def test_define_object_like(self):
        context = CCodeParsingContext()
        input = []
        input.append('#define a b')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( Grammar.LITERAL, actualOutput[2].type)
        self.assertEqual( 'b', actualOutput[2].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[3].type)

    def test_define_function_like(self):
        context = CCodeParsingContext()
        input = []
        input.append('#define a() b')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.FUNCTION_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( Grammar.PARENTHESIS_LEFT, actualOutput[2].type)
        self.assertEqual( Grammar.PARENTHESIS_RIGHT, actualOutput[3].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[4].type)
        self.assertEqual( 'b', actualOutput[4].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[5].type)

    def test_define_function_like_param(self):
        context = CCodeParsingContext()
        input = []
        input.append('#define a(x) b')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.FUNCTION_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( Grammar.PARENTHESIS_LEFT, actualOutput[2].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[3].type)
        self.assertEqual( 'x', actualOutput[3].literalValue)
        self.assertEqual( Grammar.PARENTHESIS_RIGHT, actualOutput[4].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[5].type)
        self.assertEqual( 'b', actualOutput[5].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[6].type)

    def test_define_function_like_param_2(self):
        context = CCodeParsingContext()
        input = []
        input.append('#define a(x,y) b')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.FUNCTION_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( Grammar.PARENTHESIS_LEFT, actualOutput[2].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[3].type)
        self.assertEqual( 'x', actualOutput[3].literalValue)
        self.assertEqual( Grammar.COMMA, actualOutput[4].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[5].type)
        self.assertEqual( 'y', actualOutput[5].literalValue)
        self.assertEqual( Grammar.PARENTHESIS_RIGHT, actualOutput[6].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[7].type)
        self.assertEqual( 'b', actualOutput[7].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[8].type)

    def test_define_function_like_param_2_spaces(self):
        context = CCodeParsingContext()
        input = []
        input.append('#define a( x , y ) b')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.FUNCTION_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( Grammar.PARENTHESIS_LEFT, actualOutput[2].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[3].type)
        self.assertEqual( 'x', actualOutput[3].literalValue)
        self.assertEqual( Grammar.COMMA, actualOutput[4].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[5].type)
        self.assertEqual( 'y', actualOutput[5].literalValue)
        self.assertEqual( Grammar.PARENTHESIS_RIGHT, actualOutput[6].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[7].type)
        self.assertEqual( 'b', actualOutput[7].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[8].type)

    def test_define_function_like_param_3(self):
        context = CCodeParsingContext()
        input = []
        input.append('#define a(x,y,z) b')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.FUNCTION_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( Grammar.PARENTHESIS_LEFT, actualOutput[2].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[3].type)
        self.assertEqual( 'x', actualOutput[3].literalValue)
        self.assertEqual( Grammar.COMMA, actualOutput[4].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[5].type)
        self.assertEqual( 'y', actualOutput[5].literalValue)
        self.assertEqual( Grammar.COMMA, actualOutput[6].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[7].type)
        self.assertEqual( 'z', actualOutput[7].literalValue)
        self.assertEqual( Grammar.PARENTHESIS_RIGHT, actualOutput[8].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[9].type)
        self.assertEqual( 'b', actualOutput[9].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[10].type)

    def test_define_function_like_param_3_spaces(self):
        context = CCodeParsingContext()
        input = []
        input.append('#define a(  x  ,  y  ,  z  ) b')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.FUNCTION_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( Grammar.PARENTHESIS_LEFT, actualOutput[2].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[3].type)
        self.assertEqual( 'x', actualOutput[3].literalValue)
        self.assertEqual( Grammar.COMMA, actualOutput[4].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[5].type)
        self.assertEqual( 'y', actualOutput[5].literalValue)
        self.assertEqual( Grammar.COMMA, actualOutput[6].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[7].type)
        self.assertEqual( 'z', actualOutput[7].literalValue)
        self.assertEqual( Grammar.PARENTHESIS_RIGHT, actualOutput[8].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[9].type)
        self.assertEqual( 'b', actualOutput[9].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[10].type)

    def test_define_variadic(self):
        context = CCodeParsingContext()
        input = []
        input.append('#define a(...) b')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.FUNCTION_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( Grammar.PARENTHESIS_LEFT, actualOutput[2].type)
        self.assertEqual( Grammar.VARIADIC_ARGS, actualOutput[3].type)
        self.assertEqual( Grammar.PARENTHESIS_RIGHT, actualOutput[4].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[5].type)
        self.assertEqual( 'b', actualOutput[5].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[6].type)

    def test_define_variadic_param_1(self):
        context = CCodeParsingContext()
        input = []
        input.append('#define a(x,...) b')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.FUNCTION_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( Grammar.PARENTHESIS_LEFT, actualOutput[2].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[3].type)
        self.assertEqual( 'x', actualOutput[3].literalValue)
        self.assertEqual( Grammar.COMMA, actualOutput[4].type)
        self.assertEqual( Grammar.VARIADIC_ARGS, actualOutput[5].type)
        self.assertEqual( Grammar.PARENTHESIS_RIGHT, actualOutput[6].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[7].type)
        self.assertEqual( 'b', actualOutput[7].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[8].type)

    def test_define_variadic_param_1_spaces(self):
        context = CCodeParsingContext()
        input = []
        input.append('#define a( x , ... ) b')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.FUNCTION_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( Grammar.PARENTHESIS_LEFT, actualOutput[2].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[3].type)
        self.assertEqual( 'x', actualOutput[3].literalValue)
        self.assertEqual( Grammar.COMMA, actualOutput[4].type)
        self.assertEqual( Grammar.VARIADIC_ARGS, actualOutput[5].type)
        self.assertEqual( Grammar.PARENTHESIS_RIGHT, actualOutput[6].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[7].type)
        self.assertEqual( 'b', actualOutput[7].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[8].type)

    def test_define_variadic_param_2(self):
        context = CCodeParsingContext()
        input = []
        input.append('#define a(x,y,...) b')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.FUNCTION_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( Grammar.PARENTHESIS_LEFT, actualOutput[2].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[3].type)
        self.assertEqual( 'x', actualOutput[3].literalValue)
        self.assertEqual( Grammar.COMMA, actualOutput[4].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[5].type)
        self.assertEqual( 'y', actualOutput[5].literalValue)
        self.assertEqual( Grammar.COMMA, actualOutput[6].type)
        self.assertEqual( Grammar.VARIADIC_ARGS, actualOutput[7].type)
        self.assertEqual( Grammar.PARENTHESIS_RIGHT, actualOutput[8].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[9].type)
        self.assertEqual( 'b', actualOutput[9].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[10].type)

    def test_define_variadic_param_2_spaces(self):
        context = CCodeParsingContext()
        input = []
        input.append('#define a( x , y , ... ) b')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.FUNCTION_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( Grammar.PARENTHESIS_LEFT, actualOutput[2].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[3].type)
        self.assertEqual( 'x', actualOutput[3].literalValue)
        self.assertEqual( Grammar.COMMA, actualOutput[4].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[5].type)
        self.assertEqual( 'y', actualOutput[5].literalValue)
        self.assertEqual( Grammar.COMMA, actualOutput[6].type)
        self.assertEqual( Grammar.VARIADIC_ARGS, actualOutput[7].type)
        self.assertEqual( Grammar.PARENTHESIS_RIGHT, actualOutput[8].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[9].type)
        self.assertEqual( 'b', actualOutput[9].literalValue)

        self.assertEqual( Grammar.EOL, actualOutput[10].type)

    def test_define_object_like_empty_parenthesis_impl(self):
        context = CCodeParsingContext()
        input = []
        input.append('#define a ()')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( Grammar.PARENTHESIS_LEFT, actualOutput[2].type)
        self.assertEqual( Grammar.PARENTHESIS_RIGHT, actualOutput[3].type)

        self.assertEqual( Grammar.EOL, actualOutput[4].type)

    def test_define_object_like_constant_in_parenthesis(self):
        context = CCodeParsingContext()
        input = []
        input.append('#define aa (5)')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'aa', actualOutput[1].literalValue)
        self.assertEqual( Grammar.PARENTHESIS_LEFT, actualOutput[2].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[3].type)
        self.assertEqual( '5', actualOutput[3].literalValue)
        self.assertEqual( Grammar.PARENTHESIS_RIGHT, actualOutput[4].type)

        self.assertEqual( Grammar.EOL, actualOutput[5].type)

    def test_define_object_like_float_constant_in_parenthesis(self):
        context = CCodeParsingContext()
        input = []
        input.append('#define a (5.5)')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( Grammar.PARENTHESIS_LEFT, actualOutput[2].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[3].type)
        self.assertEqual( '5.5', actualOutput[3].literalValue)
        self.assertEqual( Grammar.PARENTHESIS_RIGHT, actualOutput[4].type)

        self.assertEqual( Grammar.EOL, actualOutput[5].type)

    def test_define_object_like_string_constant(self):
        context = CCodeParsingContext()
        input = []
        input.append('#define a "str"')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[2].type)
        self.assertEqual( Grammar.STRING, actualOutput[3].type)
        self.assertEqual( 'str', actualOutput[3].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[4].type)

        self.assertEqual( Grammar.EOL, actualOutput[5].type)

    def test_define_object_like_str_const_like_variadic(self):
        context = CCodeParsingContext()
        input = []
        input.append('#define a "..."')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[2].type)
        self.assertEqual( Grammar.STRING, actualOutput[3].type)
        self.assertEqual( '...', actualOutput[3].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[4].type)

        self.assertEqual( Grammar.EOL, actualOutput[5].type)

    def test_define_function_like_sum(self):
        context = CCodeParsingContext()
        input = []
        input.append('#define sum(x,y) (x)+(y)')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.FUNCTION_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'sum', actualOutput[1].literalValue)
        self.assertEqual( Grammar.PARENTHESIS_LEFT, actualOutput[2].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[3].type)
        self.assertEqual( 'x', actualOutput[3].literalValue)
        self.assertEqual( Grammar.COMMA, actualOutput[4].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[5].type)
        self.assertEqual( 'y', actualOutput[5].literalValue)
        self.assertEqual( Grammar.PARENTHESIS_RIGHT, actualOutput[6].type)
        self.assertEqual( Grammar.PARENTHESIS_LEFT, actualOutput[7].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[8].type)
        self.assertEqual( 'x', actualOutput[8].literalValue)
        self.assertEqual( Grammar.PARENTHESIS_RIGHT, actualOutput[9].type)
        self.assertEqual( Grammar.ADDITION, actualOutput[10].type)
        self.assertEqual( Grammar.PARENTHESIS_LEFT, actualOutput[11].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[12].type)
        self.assertEqual( 'y', actualOutput[12].literalValue)
        self.assertEqual( Grammar.PARENTHESIS_RIGHT, actualOutput[13].type)

        self.assertEqual( Grammar.EOL, actualOutput[14].type)

    def test_define_function_like_sum_spaces(self):
        context = CCodeParsingContext()
        input = []
        input.append('#define sum( x , y ) ( x ) + ( y )')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.FUNCTION_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'sum', actualOutput[1].literalValue)
        self.assertEqual( Grammar.PARENTHESIS_LEFT, actualOutput[2].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[3].type)
        self.assertEqual( 'x', actualOutput[3].literalValue)
        self.assertEqual( Grammar.COMMA, actualOutput[4].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[5].type)
        self.assertEqual( 'y', actualOutput[5].literalValue)
        self.assertEqual( Grammar.PARENTHESIS_RIGHT, actualOutput[6].type)
        self.assertEqual( Grammar.PARENTHESIS_LEFT, actualOutput[7].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[8].type)
        self.assertEqual( 'x', actualOutput[8].literalValue)
        self.assertEqual( Grammar.PARENTHESIS_RIGHT, actualOutput[9].type)
        self.assertEqual( Grammar.ADDITION, actualOutput[10].type)
        self.assertEqual( Grammar.PARENTHESIS_LEFT, actualOutput[11].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[12].type)
        self.assertEqual( 'y', actualOutput[12].literalValue)
        self.assertEqual( Grammar.PARENTHESIS_RIGHT, actualOutput[13].type)

        self.assertEqual( Grammar.EOL, actualOutput[14].type)

    def test_define_wrong_function_like_sum(self):
        context = CCodeParsingContext()
        input = []
        input.append('#define sum (x,y) (x)+(y)')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'sum', actualOutput[1].literalValue)
        self.assertEqual( Grammar.PARENTHESIS_LEFT, actualOutput[2].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[3].type)
        self.assertEqual( 'x', actualOutput[3].literalValue)
        self.assertEqual( Grammar.COMMA, actualOutput[4].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[5].type)
        self.assertEqual( 'y', actualOutput[5].literalValue)
        self.assertEqual( Grammar.PARENTHESIS_RIGHT, actualOutput[6].type)
        self.assertEqual( Grammar.PARENTHESIS_LEFT, actualOutput[7].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[8].type)
        self.assertEqual( 'x', actualOutput[8].literalValue)
        self.assertEqual( Grammar.PARENTHESIS_RIGHT, actualOutput[9].type)
        self.assertEqual( Grammar.ADDITION, actualOutput[10].type)
        self.assertEqual( Grammar.PARENTHESIS_LEFT, actualOutput[11].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[12].type)
        self.assertEqual( 'y', actualOutput[12].literalValue)
        self.assertEqual( Grammar.PARENTHESIS_RIGHT, actualOutput[13].type)

        self.assertEqual( Grammar.EOL, actualOutput[14].type)
