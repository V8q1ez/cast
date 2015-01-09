__author__ = 'V8q1ez'

from src.castle.incantations import *

class prince():
    def __init__(self):
        self._outputText = []

    def buildFormattedText(self, tokens):
        currentLine = ''
        for t in tokens:
            if t.type == OBJECT_LIKE_MACRO:
                currentLine += '#define '
            elif t.type == LITERAL:
                currentLine += t.literalValue.upper()
            elif t.type == PARENTHESIS_LEFT:
                currentLine += ' ('
            elif t.type == PARENTHESIS_RIGHT:
                currentLine += ')'

        self._outputText.append(currentLine)

        return self._outputText
