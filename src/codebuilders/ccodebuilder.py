__author__ = 'V8q1ez'

from src.codebuilders.macrobuilder import MacroBuilder, MacroBuilderContext
from src.codebuilders.typedefbuilder import TypeDefBuilder, TypedefBuilderContext
from src.castle.ccodeparser import Grammar


class CCodeBuildingContext():
    def __init__(self):
        self.outputText = []
        self.currentLine = ''
        self.codingRules = None
        self.previousBlockType = Grammar.UNKNOWN


class CSyntaxError(RuntimeError):
    def __init__(self, arg):
        self.args = arg


class CCodeBuilder():
    def __init__(self):
        pass

    def buildFormattedText(self, tokenList, buildingContext):
        index = 0
        buildingContext.previousBlockType = Grammar.UNKNOWN
        while index < len(tokenList):
            t = tokenList[index]

            if t.type == Grammar.OBJECT_LIKE_MACRO:
                localContext = MacroBuilderContext()
                index = MacroBuilder.build(tokenList, index, buildingContext, localContext)
                buildingContext.previousBlockType = t.type

            elif t.type == Grammar.TYPEDEF:
                localContext = TypedefBuilderContext()
                index = TypeDefBuilder.build(tokenList, index, buildingContext, localContext)
                buildingContext.previousBlockType = t.type

            index += 1

        buildingContext.outputText.append(buildingContext.currentLine)

        return buildingContext.outputText
