__author__ = 'V8q1ez'


class EnumTypeDefinitionCodingRules():
    def handle_space_before_opening_brace(self):
        return '\n'

    def handle_space_before_closing_brace(self):
        return '\n'

    def handle_space_after_closing_brace(self):
        return ''

    def handle_space_before_next_element(self):
        return '\n    '

class CodingRules():
    def __init__(self, enum):
        self.enum = enum

    def handle_macros_name(self, name):
        return name

    def handle_enum_name(self, name):
        return name
