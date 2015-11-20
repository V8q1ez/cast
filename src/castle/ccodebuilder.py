__author__ = 'V8q1ez'

from src.castle.codingrules import CodingRules
from src.castle.ccodeparser import Grammar

class CCodeBuildingContext():
    def __init__(self):
        self.outputText = []
        self.currentLine = ''
        self.isMacrosNameHandled = False

class CCodeBuilder():
    def __init__(self, codingRules):
        self._codingRules = codingRules

    def buildFormattedText(self, tokenList, buildingContext):
        for t in tokenList:
            if t.type == Grammar.OBJECT_LIKE_MACRO:
                buildingContext.currentLine += '#define '

            elif t.type == Grammar.LITERAL:
                if buildingContext.isMacrosNameHandled:
                    buildingContext.currentLine += t.literalValue
                else:
                    buildingContext.currentLine += self._codingRules.handle_macros_name(t.literalValue)
                    buildingContext.isMacrosNameHandled = True

            elif t.type == Grammar.PARENTHESIS_LEFT:
                buildingContext.currentLine += ' ('
            elif t.type == Grammar.PARENTHESIS_RIGHT:
                buildingContext.currentLine += ')'

        buildingContext.outputText.append(buildingContext.currentLine)

        return buildingContext.outputText
