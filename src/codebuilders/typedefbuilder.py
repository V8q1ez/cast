__author__ = 'V8q1ez'

from src.castle.ccodeparser import Grammar, CToken

class TypedefBuilderContext():
    def __init__(self):
        self.bodyIndex = 0
        self.activeBlock = []


class TypeDefBuilder():
    @classmethod
    def build(self, gContext, lContext):

        if lContext.activeBlock[1].type == Grammar.ENUM:
            self._buildEnumTypeDefinitionBlock(gContext, lContext)
            gContext.currentLine += '\n'

    @classmethod
    def _buildEnumTypeDefinitionBlock(self, gContext, lContext):
        assert isinstance(lContext, TypedefBuilderContext)
        gContext.currentLine += 'typedef enum'
        index = 2
        isAssignmentHandlingRequired = False
        wasBodyProcessed = False
        while index < len(lContext.activeBlock):

            t = lContext.activeBlock[index]
            assert isinstance(t, CToken)

            if t.type == Grammar.BRACE_LEFT:
                lContext.bodyIndex += 1
                gContext.currentLine += \
                    gContext.codingRules.enum.get_space_before_opening_brace()
                gContext.currentLine += '{'

            if t.type == Grammar.BRACE_RIGHT:
                lContext.bodyIndex -= 1
                if lContext.bodyIndex == 0:
                    wasBodyProcessed = True
                gContext.currentLine += \
                    gContext.codingRules.enum.get_space_before_closing_brace()
                gContext.currentLine += '}'
                gContext.currentLine += \
                    gContext.codingRules.enum.get_space_after_closing_brace()

            elif t.type == Grammar.LITERAL:
                if lContext.bodyIndex != 0:
                    if isAssignmentHandlingRequired:
                        isAssignmentHandlingRequired = False
                    else:
                        gContext.currentLine += \
                            gContext.codingRules.enum.get_space_before_next_element()
                else:
                    if not wasBodyProcessed:
                        gContext.currentLine += gContext.codingRules.enum.get_space_before_type()

                gContext.currentLine += t.literalValue

            elif t.type == Grammar.COMMA:
                gContext.currentLine += ','

            elif t.type == Grammar.ASSIGNMENT:
                isAssignmentHandlingRequired = True
                gContext.currentLine += \
                    gContext.codingRules.enum.get_space_before_assignment()
                gContext.currentLine += '='
                gContext.currentLine += \
                    gContext.codingRules.enum.get_space_after_assignment()

            elif t.type == Grammar.SINGLE_LINE_COMMENT:
                gContext.currentLine += \
                    gContext.codingRules.enum.get_min_space_before_comment()
                gContext.currentLine += '//' + t.literalValue

            elif t.type == Grammar.MULTI_LINE_COMMENT_START:
                gContext.currentLine += \
                    gContext.codingRules.enum.get_min_space_before_comment()
                gContext.currentLine += '/*'

            elif t.type == Grammar.MULTI_LINE_COMMENT_LINE:
                gContext.currentLine += t.literalValue

            elif t.type == Grammar.MULTI_LINE_COMMENT_END:
                gContext.currentLine += '*/'

            elif t.type == Grammar.SEMICOLON:
                gContext.currentLine += ';'
                return index
            index += 1
        return
