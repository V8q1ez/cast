__author__ = 'V8q1ez'

import unittest
import mock


from src.castle.ccodeparser import CCodeParser
from src.castle.ccodebuilder import CCodeBuilder
from src.castle.codingrules import CodingRules
from src.castle.ccodeparser import Grammar
from src.castle.ccodeparser import CCodeParsingContext
from src.castle.ccodebuilder import CCodeBuildingContext

class CCodeBuilderDefine(unittest.TestCase):
    def setUp(self):
        self._parser = CCodeParser(Grammar())
        pass

    def test_define_nominal(self):
        builder = CCodeBuilder(CodingRules())
        pContext = CCodeParsingContext()
        bContext = CCodeBuildingContext()

        inputText = """#define A (5)\n"""
        expectedOutput = """#define A (5)\n"""

        actualOutput = builder.buildFormattedText( self._parser.parseText(inputText.splitlines(), pContext), bContext )
        self.assertEqual( expectedOutput.splitlines(), actualOutput )


    @mock.patch.object(CodingRules, 'handle_macros_name')
    def test_define_lower_case_literal(self, coding_rules_mock):
        builder = CCodeBuilder(coding_rules_mock)
        pContext = CCodeParsingContext()
        bContext = CCodeBuildingContext()

        coding_rules_mock.handle_macros_name.return_value = 'LITERAL'

        inputText = """#define literal (5)\n"""
        expectedOutput = """#define LITERAL (5)\n"""

        actualOutput = builder.buildFormattedText( self._parser.parseText(inputText.splitlines(), pContext), bContext )
        self.assertEqual( expectedOutput.splitlines(), actualOutput )


    @mock.patch.object(CodingRules, 'handle_macros_name')
    def test_define_lower_case_literal_allowed(self, coding_rules_mock):
        builder = CCodeBuilder(coding_rules_mock)
        pContext = CCodeParsingContext()
        bContext = CCodeBuildingContext()
        coding_rules_mock.handle_macros_name.return_value = 'literal'

        inputText = """#define literal (5)\n"""
        expectedOutput = """#define literal (5)\n"""

        actualOutput = builder.buildFormattedText( self._parser.parseText(inputText.splitlines(), pContext), bContext )
        self.assertEqual( expectedOutput.splitlines(), actualOutput )
