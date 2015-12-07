from src.codebuilders.macrobuilder import MacroBuilder
from src.codebuilders.typedefbuilder import TypeDefBuilder

__author__ = 'V8q1ez'

from src.castle.codingrules import CodingRules
from src.castle.ccodeparser import Grammar

class CCodeBuildingContext():
    def __init__(self):
        self.outputText = []
        self.currentLine = ''
        self.isMacrosNameHandled = False
        self.codingRules = None

class CSyntaxError(RuntimeError):
   def __init__(self, arg):
      self.args = arg

class CCodeBuilder():
    def __init__(self):
        pass

    def buildFormattedText(self, tokenList, buildingContext):
        index = 0
        while index < len(tokenList):
            t = tokenList[index]

            if t.type == Grammar.OBJECT_LIKE_MACRO:
                index = MacroBuilder.build(tokenList, index, buildingContext)

            elif t.type == Grammar.TYPEDEF:
                index = TypeDefBuilder.build(tokenList, index, buildingContext)

            index += 1

        buildingContext.outputText.append(buildingContext.currentLine)

        return buildingContext.outputText

