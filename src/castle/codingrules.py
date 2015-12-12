__author__ = 'V8q1ez'


class EnumTypeDefinitionDefaultCodingRules():
    def get_space_before_opening_brace(self):
        return '\n'

    def get_space_before_closing_brace(self):
        return '\n'

    def get_space_after_closing_brace(self):
        return ''

    def get_space_before_next_element(self):
        return '\n    '

    def get_space_before_assignment(self):
        return ' '

    def get_space_after_assignment(self):
        return ' '

    def get_min_space_before_comment(self):
        return '    '

    def get_space_before_type(self):
        return ' '

class DefaultCodingRules():
    def __init__(self, enum):
        self.enum = enum

    def handle_macros_name(self, name):
        return name

    def handle_enum_name(self, name):
        return name

    def get_space_between_similar_blocks(self):
        return '\n'
