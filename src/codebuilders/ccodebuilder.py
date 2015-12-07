__author__ = 'V8q1ez'

from src.codebuilders.macrobuilder import MacroBuilder, MacroBuilderContext
from src.codebuilders.typedefbuilder import TypeDefBuilder
from src.castle.ccodeparser import Grammar

class CCodeBuildingContext():
    def __init__(self):
        self.outputText = []
        self.currentLine = ''
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
                localContext = MacroBuilderContext()
                index = MacroBuilder.build(tokenList, index, buildingContext, localContext)

            elif t.type == Grammar.TYPEDEF:
                index = TypeDefBuilder.build(tokenList, index, buildingContext)

            index += 1

        buildingContext.outputText.append(buildingContext.currentLine)

        return buildingContext.outputText

