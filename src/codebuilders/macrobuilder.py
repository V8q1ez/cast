__author__ = 'V8q1ez'

from src.castle.ccodeparser import Grammar

class MacroBuilderContext():
    def __init__(self):
        self.isMacrosNameHandled = False

class MacroBuilder():
    @classmethod
    def build(self, tokenList, index, gContext, lContext):
        return self._buildObjectLikeMacro(tokenList, index, gContext, lContext)

    @classmethod
    def _buildObjectLikeMacro(self, tokenList, index, gContext, lContext):
        gContext.currentLine += '#define '
        index += 1
        while index < len(tokenList):
            t = tokenList[index]
            if t.type == Grammar.LITERAL:
                if lContext.isMacrosNameHandled:
                    gContext.currentLine += t.literalValue
                else:
                    gContext.currentLine += gContext.codingRules.handle_macros_name(t.literalValue)
                    lContext.isMacrosNameHandled = True

            elif t.type == Grammar.PARENTHESIS_LEFT:
                gContext.currentLine += ' ('
            elif t.type == Grammar.PARENTHESIS_RIGHT:
                gContext.currentLine += ')'
            index += 1
        return index