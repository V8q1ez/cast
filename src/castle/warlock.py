__author__ = 'V8q1ez'

from src.castle.cinderella import *

class warlock():
    def __init__(self):
        pass

    def areFilesEquivalent(self, left_file_text, right_file_text):
        left_file_tokens = cinderella().parseText(left_file_text)
        right_file_tokens = cinderella().parseText(right_file_text)

        lf_index = 0
        rf_index = 0

        while lf_index < len(left_file_tokens) and rf_index < len(right_file_tokens):
            if left_file_tokens[lf_index].type != right_file_tokens[rf_index].type:
                if right_file_tokens[rf_index].type == SINGLE_LINE_COMMENT:
                    rf_index += 1
                    continue
                elif left_file_tokens[lf_index].type == SINGLE_LINE_COMMENT:
                    lf_index += 1
                    continue
                return False
            else:
                if left_file_tokens[lf_index].type == LITERAL:
                    if left_file_tokens[lf_index].literalValue != right_file_tokens[rf_index].literalValue:
                        return False
                elif left_file_tokens[lf_index].type == STRING:
                    if left_file_tokens[lf_index].literalValue != right_file_tokens[rf_index].literalValue:
                        return False

            lf_index += 1
            rf_index += 1

        return True