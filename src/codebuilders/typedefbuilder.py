__author__ = 'V8q1ez'

from src.castle.codingrules import CodingRules
from src.castle.ccodeparser import Grammar

class TypeDefBuilder():
    @classmethod
    def build(self, tokenList, index, context):
        context.currentLine += 'typedef '
        index += 1
        while index < len(tokenList):
            t = tokenList[index]
            if t.type == Grammar.ENUM:
                index = self._buildEnumTypeDefinition(tokenList, index, context)
            else: index += 1
        return index

    @classmethod
    def _buildEnumTypeDefinition(self, tokenList, index, context):
        context.currentLine += 'enum{ENUM_VALUE_1}ENUM_TYPE_NAME_E;'
        index += 1
        while index < len(tokenList):
            t = tokenList[index]
            """if t == Grammar.PARENTHESIS_LEFT:
                context.currentLine += \
                    context.codingRules.handle_space_before_opening_parenthesis()
                context.currentLine += '{'
            elif t == Grammar.LITERAL:
                pass
            """
            if t == Grammar.SEMICOLON:
                return index
            index += 1
        return index