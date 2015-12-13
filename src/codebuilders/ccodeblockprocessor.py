__author__ = 'V8q1ez'

from src.castle.ccodeparser import Grammar, CToken


class CCodeBlockProcessorContext:
    def __init__(self, previous_block_type):
        self.activeBlock = []
        self.activeBlockType = Grammar.UNKNOWN
        self.previousBlockType = previous_block_type


class CCodeBlockProcessor:

    @classmethod
    def popBlock(self, tokenList, index, context):
        assert isinstance(context, CCodeBlockProcessorContext)
        context.activeBlock = []
        context.activeBlock.append(tokenList[index])  # typedef
        context.activeBlockType = Grammar.TYPEDEF # TODO
        index += 1
        isClosingBraceFound = False
        while index < len(tokenList):
            t = tokenList[index]
            assert isinstance(t, CToken)
            context.activeBlock.append(tokenList[index])
            if t.type == Grammar.BRACE_LEFT:
                isClosingBraceFound = True
            elif isClosingBraceFound and t.type == Grammar.SEMICOLON:
                break
            index += 1
        # make all ending EOL part of the block
        if len(tokenList)>index and tokenList[index +1].type == Grammar.EOL:
            index += 1
            while index < len(tokenList):
                if tokenList[index].type != Grammar.EOL:
                    index -= 1
                    break
                index += 1

        return index

    @classmethod
    def AnalyseAndCorrectBlock(self, context):
        assert isinstance(context, CCodeBlockProcessorContext)
        index = 0
        elementIndex = 0
        commentIndex = 0
        mlCommentIndex = 0
        bodyIndex = 0
        while index < len(context.activeBlock):
            t = context.activeBlock[index]
            assert isinstance(t, CToken)
            if t.type == Grammar.BRACE_LEFT:
                bodyIndex += 1
            elif t.type == Grammar.BRACE_RIGHT:
                bodyIndex -= 1
            elif t.type == Grammar.LITERAL:
                if bodyIndex > 0:
                    elementIndex = index
            elif t.type == Grammar.SINGLE_LINE_COMMENT:
                commentIndex = index
            elif t.type == Grammar.MULTI_LINE_COMMENT_START:
                mlCommentIndex = index
            elif t.type == Grammar.COMMA:
                if mlCommentIndex != 0:
                    # issue: element /* comment */ EOL ,
                    if elementIndex + 1 == mlCommentIndex and mlCommentIndex + 4 == index:
                        context.activeBlock[mlCommentIndex], context.activeBlock[index] = \
                            context.activeBlock[index], context.activeBlock[mlCommentIndex]
                        context.activeBlock[mlCommentIndex + 1], context.activeBlock[index] = \
                            context.activeBlock[index], context.activeBlock[mlCommentIndex + 1]
                        context.activeBlock[mlCommentIndex + 2], context.activeBlock[index] = \
                            context.activeBlock[index], context.activeBlock[mlCommentIndex + 2]
                else:
                    # issue: element // comment EOL ,
                    if elementIndex + 1 == commentIndex and commentIndex + 2 == index:
                        context.activeBlock[commentIndex], context.activeBlock[index] = \
                            context.activeBlock[index], context.activeBlock[commentIndex]
                        context.activeBlock[index], context.activeBlock[index - 1] = \
                            context.activeBlock[index - 1], context.activeBlock[index]

            index += 1