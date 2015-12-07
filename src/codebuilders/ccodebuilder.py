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
                index = self._buildObjectLikeMacro(tokenList, index, buildingContext)

            elif t.type == Grammar.TYPEDEF:
                index = self._buildTypeDefinition(tokenList, index, buildingContext)

            index += 1

        buildingContext.outputText.append(buildingContext.currentLine)

        return buildingContext.outputText

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

    def _buildTypeDefinition(self, tokenList, index, context):
        context.currentLine += 'typedef '
        index += 1
        while index < len(tokenList):
            t = tokenList[index]
            if t.type == Grammar.ENUM:
                index = self._buildEnumTypeDefinition(tokenList, index, context)
            else: index += 1
        return index

    def _buildEnumTypeDefinition(self, tokenList, index, context):
        context.currentLine += 'enum{ENUM_VALUE_1}ENUM_TYPE_NAME_E;'
        index += 1
        while index < len(tokenList):
            t = tokenList[index]
            """if t == Grammar.PARENTHESIS_LEFT:
                context.currentLine += \
                    context.codingRules.handle_space_before_opening_parenthesis()
                context.currentLine += '{'
            elif t == Grammar.LITERAL:
                pass
            """
            if t == Grammar.SEMICOLON:
                return index
            index += 1
        return index

