__author__ = 'V8q1ez'

import unittest
import mock


from src.castle.ccodeparser import CCodeParser
from src.castle.ccodebuilder import CCodeBuilder
from src.castle.codingrules import CodingRules
from src.castle.ccodeparser import Grammar
from src.castle.ccodeparser import CCodeParsingContext
from src.castle.ccodebuilder import CCodeBuildingContext


class CodingRulesEnum(CodingRules):
    def handle_enum_name(self, name):
        return 'ENUM_TYPE_NAME_E'


class CCodeBuilderEnum(unittest.TestCase):
    def setUp(self):
        self._parser = CCodeParser(Grammar())
        pass

    def test_enum_single_line(self):
        builder = CCodeBuilder(CodingRulesEnum())
        pContext = CCodeParsingContext()
        bContext = CCodeBuildingContext()

        inputText = "typedef enum{ENUM_VALUE_1}enum_type_name;"
        expectedOutput = "typedef enum{ENUM_VALUE_1}ENUM_TYPE_NAME_E;"

        actualOutput = builder.buildFormattedText( self._parser.parseText(inputText.splitlines(), pContext), bContext )
        self.assertEqual( expectedOutput.splitlines(), actualOutput )

