__author__ = 'V8q1ez'

from src.castle.codingrules import CodingRules
from src.castle.ccodeparser import Grammar

class prince():
    def __init__(self, legalist):
        self._outputText = []
        self._legalist = legalist

    def buildFormattedText(self, tokens):
        currentLine = ''
        isMacrosNameHandled = False
        for t in tokens:
            if t.type == Grammar.OBJECT_LIKE_MACRO:
                currentLine += '#define '

            elif t.type == Grammar.LITERAL:
                if isMacrosNameHandled:
                    currentLine += t.literalValue
                else:
                    currentLine += self._legalist.handle_macros_name( t.literalValue )
                    isMacrosNameHandled = True

            elif t.type == Grammar.PARENTHESIS_LEFT:
                currentLine += ' ('
            elif t.type == Grammar.PARENTHESIS_RIGHT:
                currentLine += ')'

        self._outputText.append(currentLine)

        return self._outputText
