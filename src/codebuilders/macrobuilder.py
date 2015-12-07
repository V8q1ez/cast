__author__ = 'V8q1ez'

from src.castle.codingrules import CodingRules
from src.castle.ccodeparser import Grammar

class MacroBuilder():
    @classmethod
    def build(self, tokenList, index, context):
        return self._buildObjectLikeMacro(tokenList, index, context)

    @classmethod
    def _buildObjectLikeMacro(self, tokenList, index, context):
        context.currentLine += '#define '
        index += 1
        while index < len(tokenList):
            t = tokenList[index]
            if t.type == Grammar.LITERAL:
                if context.isMacrosNameHandled:
                    context.currentLine += t.literalValue
                else:
                    context.currentLine += context.codingRules.handle_macros_name(t.literalValue)
                    context.isMacrosNameHandled = True

            elif t.type == Grammar.PARENTHESIS_LEFT:
                context.currentLine += ' ('
            elif t.type == Grammar.PARENTHESIS_RIGHT:
                context.currentLine += ')'
            index += 1
        return index