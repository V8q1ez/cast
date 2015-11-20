__author__ = 'V8q1ez'

from src.castle.ccodeparser import Grammar
from src.castle.ccodeparser import CCodeParser
from src.castle.ccodeparser import CCodeParsingContext

class warlock():
    def __init__(self, grammar):
        self._grammar = grammar
        self.isMultiLineCommentStartedInRight = False
        self.isMultiLineCommentStartedInLeft = False

    def areFilesEquivalent(self, left_file_text, right_file_text):
        parser = CCodeParser(self._grammar)
        left_file_tokens = parser.parseText(left_file_text, CCodeParsingContext())
        right_file_tokens = parser.parseText(right_file_text, CCodeParsingContext())

        lf_index = 0
        rf_index = 0

        while lf_index < len(left_file_tokens) and rf_index < len(right_file_tokens):
            if self.isMultiLineCommentStartedInRight == True:
                if right_file_tokens[rf_index].type != Grammar.MULTI_LINE_COMMENT_END:
                    rf_index += 1
                    continue
                else:
                    self.isMultiLineCommentStartedInRight = False
                    rf_index += 1
                    continue
            elif self.isMultiLineCommentStartedInLeft == True:
                if left_file_tokens[lf_index].type != Grammar.MULTI_LINE_COMMENT_END:
                    lf_index += 1
                    continue
                else:
                    self.isMultiLineCommentStartedInLeft = False
                    lf_index += 1
                    continue
            elif left_file_tokens[lf_index].type != right_file_tokens[rf_index].type:
                if left_file_tokens[lf_index].type == Grammar.EOL:
                    lf_index += 1
                    continue
                elif right_file_tokens[rf_index].type == Grammar.EOL:
                    rf_index += 1
                    continue
                elif right_file_tokens[rf_index].type == Grammar.SINGLE_LINE_COMMENT:
                    rf_index += 1
                    continue
                elif left_file_tokens[lf_index].type == Grammar.SINGLE_LINE_COMMENT:
                    lf_index += 1
                    continue
                elif right_file_tokens[rf_index].type == Grammar.MULTI_LINE_COMMENT_START:
                    self.isMultiLineCommentStartedInRight = True
                    rf_index += 1
                    continue
                elif left_file_tokens[lf_index].type == Grammar.MULTI_LINE_COMMENT_START:
                    self.isMultiLineCommentStartedInLeft = True
                    lf_index += 1
                    continue
                return False
            else:
                if left_file_tokens[lf_index].type == Grammar.LITERAL:
                    if left_file_tokens[lf_index].literalValue != right_file_tokens[rf_index].literalValue:
                        return False
                elif left_file_tokens[lf_index].type == Grammar.STRING:
                    if left_file_tokens[lf_index].literalValue != right_file_tokens[rf_index].literalValue:
                        return False

            lf_index += 1
            rf_index += 1

        return True