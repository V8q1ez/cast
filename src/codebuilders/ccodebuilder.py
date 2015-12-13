from src.codebuilders.ccodeblockprocessor import CCodeBlockProcessorContext, CCodeBlockProcessor

__author__ = 'V8q1ez'

from src.codebuilders.macrobuilder import MacroBuilder, MacroBuilderContext
from src.codebuilders.typedefbuilder import TypeDefBuilder, TypedefBuilderContext
from src.castle.ccodeparser import Grammar, CToken


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
        previous_block_type = Grammar.UNKNOWN
        while index < len(tokenList):
            ccb_context = CCodeBlockProcessorContext( previous_block_type )
            index = CCodeBlockProcessor.popBlock(tokenList, index, ccb_context)
            CCodeBlockProcessor.AnalyseAndCorrectBlock(ccb_context)

            if previous_block_type == ccb_context.activeBlockType:
                buildingContext.currentLine += buildingContext.codingRules.get_space_between_similar_blocks()

            if ccb_context.activeBlockType == Grammar.OBJECT_LIKE_MACRO:
                localContext = MacroBuilderContext()
                index = MacroBuilder.build(tokenList, index, buildingContext, localContext)
                buildingContext.previousBlockType = Grammar.UNKNOWN

            elif ccb_context.activeBlockType == Grammar.TYPEDEF:
                localContext = TypedefBuilderContext()
                localContext.activeBlock = ccb_context.activeBlock
                TypeDefBuilder.build(buildingContext, localContext)
                previous_block_type = ccb_context.activeBlockType

            index += 1

        buildingContext.outputText.append(buildingContext.currentLine)

        return buildingContext.outputText

