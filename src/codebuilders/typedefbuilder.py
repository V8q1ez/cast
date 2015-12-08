__author__ = 'V8q1ez'

from src.castle.ccodeparser import Grammar, CToken

class TypedefBuilderContext():
    def __init__(self):
        self.bodyIndex = 0
        self.isAssignmentHandlingRequired = False


class TypeDefBuilder():
    @classmethod
    def build(self, tokenList, index, gContext, lContext):
        gContext.currentLine += 'typedef '
        index += 1
        while index < len(tokenList):
            t = tokenList[index]
            if t.type == Grammar.ENUM:
                index = self._buildEnumTypeDefinition(tokenList, index, gContext, lContext)
            else: index += 1
        return index

    @classmethod
    def _buildEnumTypeDefinition(self, tokenList, index, gContext, lContext):
        assert isinstance(lContext, TypedefBuilderContext)
        gContext.currentLine += 'enum'
        index += 1
        while index < len(tokenList):

            t = tokenList[index]
            assert isinstance(t, CToken)

            if t.type == Grammar.BRACE_LEFT:
                lContext.bodyIndex += 1
                gContext.currentLine += \
                    gContext.codingRules.enum.get_space_before_opening_brace()
                gContext.currentLine += '{'

            if t.type == Grammar.BRACE_RIGHT:
                lContext.bodyIndex -= 1
                gContext.currentLine += \
                    gContext.codingRules.enum.get_space_before_closing_brace()
                gContext.currentLine += '}'
                gContext.currentLine += \
                    gContext.codingRules.enum.get_space_after_closing_brace()

            elif t.type == Grammar.LITERAL:
                if lContext.bodyIndex != 0:
                    if lContext.isAssignmentHandlingRequired:
                        lContext.isAssignmentHandlingRequired = False
                    else:
                        gContext.currentLine += \
                            gContext.codingRules.enum.get_space_before_next_element()
                gContext.currentLine += t.literalValue

            elif t.type == Grammar.COMMA:
                gContext.currentLine += ','

            elif t.type == Grammar.ASSIGNMENT:
                lContext.isAssignmentHandlingRequired = True
                gContext.currentLine += \
                        gContext.codingRules.enum.get_space_before_assignment()
                gContext.currentLine += '='
                gContext.currentLine += \
                        gContext.codingRules.enum.get_space_after_assignment()

            elif t.type == Grammar.SEMICOLON:
                gContext.currentLine += ';'
                return index
            index += 1
        return index