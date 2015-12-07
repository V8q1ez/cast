__author__ = 'V8q1ez'

import unittest

from src.castle.ccodeparser import CCodeParser
from src.castle.ccodeparser import CCodeParsingContext
from src.castle.ccodeparser import Grammar
from src.castle.codingrules import CodingRules, EnumTypeDefinitionCodingRules
from src.codebuilders.ccodebuilder import CCodeBuilder
from src.codebuilders.ccodebuilder import CCodeBuildingContext

class CCodeBuilderEnum(unittest.TestCase):
    def setUp(self):
        self._parser = CCodeParser(Grammar())
        pass

    def test_enum_simple(self):
        builder = CCodeBuilder()
        pContext = CCodeParsingContext()
        bContext = CCodeBuildingContext()

        bContext.codingRules = CodingRules( EnumTypeDefinitionCodingRules() )

        inputText = "typedef enum{ENUM_VALUE_1}ENUM_TYPE_NAME_E;"
        expectedOutput = """typedef enum
{
    ENUM_VALUE_1
}ENUM_TYPE_NAME_E;"""

        actualOutput = builder.buildFormattedText( self._parser.parseText(inputText.splitlines(), pContext), bContext )
        self.assertMultiLineEqual( expectedOutput, '\n'.join(actualOutput) )

    def test_enum_two_elements(self):
        builder = CCodeBuilder()
        pContext = CCodeParsingContext()
        bContext = CCodeBuildingContext()

        bContext.codingRules = CodingRules( EnumTypeDefinitionCodingRules() )

        inputText = "typedef enum{ENUM_VALUE_1, ENUM_VALUE_2}ENUM_TYPE_NAME_E;"
        expectedOutput = """typedef enum
{
    ENUM_VALUE_1,
    ENUM_VALUE_2
}ENUM_TYPE_NAME_E;"""

        actualOutput = builder.buildFormattedText( self._parser.parseText(inputText.splitlines(), pContext), bContext )
        self.assertMultiLineEqual( expectedOutput, '\n'.join(actualOutput) )

