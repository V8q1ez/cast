from src.codebuilders.ccodeblockprocessor import CCodeBlockProcessorContext, CCodeBlockProcessor
from src.codebuilders.macrobuilder import MacroBuilder, MacroBuilderContext
from src.codebuilders.typedefbuilder import TypeDefBuilder, TypedefBuilderContext
from src.castle.ccodeparser import Grammar


__author__ = 'V8q1ez'


class CCodeBuildingContext:
    def __init__(self):
        self.outputText = []
        self.currentLine = ''
        self.codingRules = None


class CSyntaxError(RuntimeError):
    def __init__(self, arg):
        self.args = arg


class CCodeBuilder:
    def __init__(self):
        pass

    @classmethod
    def build_from_token_list(cls, token_list, output_context):
        assert isinstance(output_context, CCodeBuildingContext)
        index = 0
        previous_block_type = Grammar.UNKNOWN
        while index < len(token_list):
            ccb_context = CCodeBlockProcessorContext(previous_block_type)
            index = CCodeBlockProcessor.popBlock(token_list, index, ccb_context)
            CCodeBlockProcessor.AnalyseAndCorrectBlock(ccb_context)

            if previous_block_type == ccb_context.activeBlockType:
                output_context.currentLine += output_context.codingRules.get_space_between_similar_blocks()

            if ccb_context.activeBlockType == Grammar.OBJECT_LIKE_MACRO:
                local_context = MacroBuilderContext()
                index = MacroBuilder.build(token_list, index, output_context, local_context)
                output_context.previousBlockType = Grammar.UNKNOWN

            elif ccb_context.activeBlockType == Grammar.TYPEDEF:
                local_context = TypedefBuilderContext()
                local_context.activeBlock = ccb_context.activeBlock
                TypeDefBuilder.build(output_context, local_context)
                previous_block_type = ccb_context.activeBlockType

            index += 1

        output_context.outputText.append(output_context.currentLine)

        return output_context.outputText
