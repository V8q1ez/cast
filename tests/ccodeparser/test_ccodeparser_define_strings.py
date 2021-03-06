__author__ = 'V8q1ez'

import unittest

from src.castle.ccodeparser import CCodeParser
from src.castle.ccodeparser import Grammar
from src.castle.ccodeparser import CCodeParsingContext


class CCodeParserDefineStrings(unittest.TestCase):
    def setUp(self):
        self._grammar = Grammar()
        self.tkz = CCodeParser(self._grammar)

    def test_define_str_space_including(self):
        context = CCodeParsingContext()
        input = []
        input.append('#define a "before after"')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[2].type)
        self.assertEqual( Grammar.STRING, actualOutput[3].type)
        self.assertEqual( 'before after', actualOutput[3].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[4].type)

        self.assertEqual( Grammar.EOL, actualOutput[5].type)

    def test_define_str_escaped_quote(self):
        context = CCodeParsingContext()
        input = []
        input.append('#define a "before\\\"after"')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[2].type)
        self.assertEqual( Grammar.STRING, actualOutput[3].type)
        self.assertEqual( 'before\\\"after', actualOutput[3].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[4].type)

        self.assertEqual( Grammar.EOL, actualOutput[5].type)

    def test_define_str_escaped_quote_spaces(self):
        context = CCodeParsingContext()
        input = []
        input.append('#define a "before \\\" after"')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[2].type)
        self.assertEqual( Grammar.STRING, actualOutput[3].type)
        self.assertEqual( 'before \\\" after', actualOutput[3].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[4].type)

        self.assertEqual( Grammar.EOL, actualOutput[5].type)

    def test_define_str_escaped_n(self):
        context = CCodeParsingContext()
        input = []
        input.append('#define a "before\\nafter"')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[2].type)
        self.assertEqual( Grammar.STRING, actualOutput[3].type)
        self.assertEqual( 'before\\nafter', actualOutput[3].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[4].type)

        self.assertEqual( Grammar.EOL, actualOutput[5].type)

    def test_define_str_escaped_n_spaces(self):
        context = CCodeParsingContext()
        input = []
        input.append('#define a "before \\n after"')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[2].type)
        self.assertEqual( Grammar.STRING, actualOutput[3].type)
        self.assertEqual( 'before \\n after', actualOutput[3].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[4].type)

        self.assertEqual( Grammar.EOL, actualOutput[5].type)

    def test_define_str_with_enum(self):
        context = CCodeParsingContext()
        input = []
        input.append('#define a "enum"')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[2].type)
        self.assertEqual( Grammar.STRING, actualOutput[3].type)
        self.assertEqual( 'enum', actualOutput[3].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[4].type)

        self.assertEqual( Grammar.EOL, actualOutput[5].type)

    def test_define_str_with_enum_spaces(self):
        context = CCodeParsingContext()
        input = []
        input.append('#define a " enum "')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[2].type)
        self.assertEqual( Grammar.STRING, actualOutput[3].type)
        self.assertEqual( ' enum ', actualOutput[3].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[4].type)

        self.assertEqual( Grammar.EOL, actualOutput[5].type)

    def test_define_str_with_braces(self):
        context = CCodeParsingContext()
        input = []
        input.append('#define a " { } "')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[2].type)
        self.assertEqual( Grammar.STRING, actualOutput[3].type)
        self.assertEqual( ' { } ', actualOutput[3].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[4].type)

        self.assertEqual( Grammar.EOL, actualOutput[5].type)

    def test_define_str_with_parentheses(self):
        context = CCodeParsingContext()
        input = []
        input.append('#define a " ( ) "')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[2].type)
        self.assertEqual( Grammar.STRING, actualOutput[3].type)
        self.assertEqual( ' ( ) ', actualOutput[3].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[4].type)

        self.assertEqual( Grammar.EOL, actualOutput[5].type)

    def test_define_str_with_assignment(self):
        context = CCodeParsingContext()
        input = []
        input.append('#define a " b=7"')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[2].type)
        self.assertEqual( Grammar.STRING, actualOutput[3].type)
        self.assertEqual( ' b=7', actualOutput[3].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[4].type)

        self.assertEqual( Grammar.EOL, actualOutput[5].type)

    def test_define_str_with_comma(self):
        context = CCodeParsingContext()
        input = []
        input.append('#define a "b,c"')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[2].type)
        self.assertEqual( Grammar.STRING, actualOutput[3].type)
        self.assertEqual( 'b,c', actualOutput[3].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[4].type)

        self.assertEqual( Grammar.EOL, actualOutput[5].type)

    def test_define_str_with_sharp(self):
        context = CCodeParsingContext()
        input = []
        input.append('#define a "b#c"')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[2].type)
        self.assertEqual( Grammar.STRING, actualOutput[3].type)
        self.assertEqual( 'b#c', actualOutput[3].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[4].type)

        self.assertEqual( Grammar.EOL, actualOutput[5].type)

    def test_define_str_with_semicolon(self):
        context = CCodeParsingContext()
        input = []
        input.append('#define a "b;c"')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[2].type)
        self.assertEqual( Grammar.STRING, actualOutput[3].type)
        self.assertEqual( 'b;c', actualOutput[3].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[4].type)

        self.assertEqual( Grammar.EOL, actualOutput[5].type)

    def test_define_str_with_struct(self):
        context = CCodeParsingContext()
        input = []
        input.append('#define a "struct"')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[2].type)
        self.assertEqual( Grammar.STRING, actualOutput[3].type)
        self.assertEqual( 'struct', actualOutput[3].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[4].type)

        self.assertEqual( Grammar.EOL, actualOutput[5].type)

    def test_define_str_with_static(self):
        context = CCodeParsingContext()
        input = []
        input.append('#define a "static"')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[2].type)
        self.assertEqual( Grammar.STRING, actualOutput[3].type)
        self.assertEqual( 'static', actualOutput[3].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[4].type)

        self.assertEqual( Grammar.EOL, actualOutput[5].type)

    def test_define_str_with_square_braces(self):
        context = CCodeParsingContext()
        input = []
        input.append('#define a " [ ] "')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[2].type)
        self.assertEqual( Grammar.STRING, actualOutput[3].type)
        self.assertEqual( ' [ ] ', actualOutput[3].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[4].type)

        self.assertEqual( Grammar.EOL, actualOutput[5].type)

    def test_define_str_with_colon_braces(self):
        context = CCodeParsingContext()
        input = []
        input.append('#define a "a:b"')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[2].type)
        self.assertEqual( Grammar.STRING, actualOutput[3].type)
        self.assertEqual( 'a:b', actualOutput[3].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[4].type)

        self.assertEqual( Grammar.EOL, actualOutput[5].type)

    def test_define_str_with_star_and_backslash(self):
        context = CCodeParsingContext()
        input = []
        input.append('#define a "a*b/c"')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[2].type)
        self.assertEqual( Grammar.STRING, actualOutput[3].type)
        self.assertEqual( 'a*b/c', actualOutput[3].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[4].type)

        self.assertEqual( Grammar.EOL, actualOutput[5].type)

    def test_define_str_with_percent(self):
        context = CCodeParsingContext()
        input = []
        input.append('#define a "5%"')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[2].type)
        self.assertEqual( Grammar.STRING, actualOutput[3].type)
        self.assertEqual( '5%', actualOutput[3].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[4].type)

        self.assertEqual( Grammar.EOL, actualOutput[5].type)

    def test_define_str_with_function_type_definition(self):
        context = CCodeParsingContext()
        input = []
        input.append('#define a "typedef void(*FOO_TYPE)(void);"')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[2].type)
        self.assertEqual( Grammar.STRING, actualOutput[3].type)
        self.assertEqual( 'typedef void(*FOO_TYPE)(void);', actualOutput[3].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[4].type)

        self.assertEqual( Grammar.EOL, actualOutput[5].type)

    def test_define_str_with_arithmetic_operations(self):
        context = CCodeParsingContext()
        input = []
        input.append('#define a "a=b+c-d"')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[2].type)
        self.assertEqual( Grammar.STRING, actualOutput[3].type)
        self.assertEqual( 'a=b+c-d', actualOutput[3].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[4].type)

        self.assertEqual( Grammar.EOL, actualOutput[5].type)

    def test_define_str_with_increments_decrements(self):
        context = CCodeParsingContext()
        input = []
        input.append('#define a "a= ++b - c++ + --d + e--"')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[2].type)
        self.assertEqual( Grammar.STRING, actualOutput[3].type)
        self.assertEqual( 'a= ++b - c++ + --d + e--', actualOutput[3].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[4].type)

        self.assertEqual( Grammar.EOL, actualOutput[5].type)

    def test_define_str_with_comparison_relational(self):
        context = CCodeParsingContext()
        input = []
        input.append('#define a "a==b c!=d e<f g>h a<=b a>=b"')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[2].type)
        self.assertEqual( Grammar.STRING, actualOutput[3].type)
        self.assertEqual( 'a==b c!=d e<f g>h a<=b a>=b', actualOutput[3].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[4].type)

        self.assertEqual( Grammar.EOL, actualOutput[5].type)

    def test_define_str_with_logical_operations(self):
        context = CCodeParsingContext()
        input = []
        input.append('#define a "!a && b || c"')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[2].type)
        self.assertEqual( Grammar.STRING, actualOutput[3].type)
        self.assertEqual( '!a && b || c', actualOutput[3].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[4].type)

        self.assertEqual( Grammar.EOL, actualOutput[5].type)

    def test_define_str_with_bitwise_operations(self):
        context = CCodeParsingContext()
        input = []
        input.append('#define a "~a & b | c ^ d << e >> f"')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[2].type)
        self.assertEqual( Grammar.STRING, actualOutput[3].type)
        self.assertEqual( '~a & b | c ^ d << e >> f', actualOutput[3].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[4].type)

        self.assertEqual( Grammar.EOL, actualOutput[5].type)

    def test_define_str_with_compound_assignments(self):
        context = CCodeParsingContext()
        input = []
        input.append('#define a "a += b -= d *= e /= f %= g &= h |= j ^= k <<= >>="')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[2].type)
        self.assertEqual( Grammar.STRING, actualOutput[3].type)
        self.assertEqual( 'a += b -= d *= e /= f %= g &= h |= j ^= k <<= >>=', actualOutput[3].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[4].type)

        self.assertEqual( Grammar.EOL, actualOutput[5].type)

    def test_define_str_with_members_and_pointers(self):
        context = CCodeParsingContext()
        input = []
        input.append('#define a "a->b"')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[2].type)
        self.assertEqual( Grammar.STRING, actualOutput[3].type)
        self.assertEqual( 'a->b', actualOutput[3].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[4].type)

        self.assertEqual( Grammar.EOL, actualOutput[5].type)

    def test_define_str_with_ternary_conditional(self):
        context = CCodeParsingContext()
        input = []
        input.append('#define a "a?b:c"')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[2].type)
        self.assertEqual( Grammar.STRING, actualOutput[3].type)
        self.assertEqual( 'a?b:c', actualOutput[3].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[4].type)

        self.assertEqual( Grammar.EOL, actualOutput[5].type)

    def test_define_str_with_other_operators(self):
        context = CCodeParsingContext()
        input = []
        input.append('#define a "sizeof(a)+ alignof(b)"')

        actualOutput = self.tkz.parseText(input, context)

        self.assertEqual( Grammar.OBJECT_LIKE_MACRO, actualOutput[0].type)
        self.assertEqual( Grammar.LITERAL, actualOutput[1].type)
        self.assertEqual( 'a', actualOutput[1].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[2].type)
        self.assertEqual( Grammar.STRING, actualOutput[3].type)
        self.assertEqual( 'sizeof(a)+ alignof(b)', actualOutput[3].literalValue)
        self.assertEqual( Grammar.QUOTE, actualOutput[4].type)

        self.assertEqual( Grammar.EOL, actualOutput[5].type)