__author__ = 'V8q1ez'

import unittest

from src.castle.ccodeparser import CCodeParser
from src.castle.ccodeparser import CCodeParsingContext
from src.castle.ccodeparser import Grammar
from src.castle.codingrules import DefaultCodingRules, EnumTypeDefinitionDefaultCodingRules
from src.codebuilders.ccodebuilder import CCodeBuilder
from src.codebuilders.ccodebuilder import CCodeBuildingContext


class CodingRulesDefine(DefaultCodingRules):
    def handle_macros_name(self, name):
        return 'LITERAL'


class CCodeBuilderDefine(unittest.TestCase):
    def setUp(self):
        self._parser = CCodeParser(Grammar())
        pass

    """def test_define_lower_case_literal_allowed(self):
        builder = CCodeBuilder()
        pContext = CCodeParsingContext()
        bContext = CCodeBuildingContext()

        bContext.codingRules = CodingRulesDefine(EnumTypeDefinitionDefaultCodingRules())

        inputText = """#define literal (5)\n"""
"""        expectedOutput = """#define LITERAL (5)\n"""
"""
        actualOutput = builder.buildFormattedText( self._parser.parseText(inputText.splitlines(), pContext), bContext )
        self.assertEqual( expectedOutput.splitlines(), actualOutput )
"""