__author__ = 'V8q1ez'

UNKNOWN = 0
OBJECT_LIKE_MACRO = 1
INCLUDE = 2
QUOTE = 3
LITERAL = 4
PARENTHESIS_LEFT = 5
PARENTHESIS_RIGHT = 6
FUNCTION_LIKE_MACRO = 7
COMMA = 8
VARIADIC_ARGS = 9
SEMICOLON = 10
STRING = 11
EOL = 12
TYPEDEF = 13
ENUM = 14
BRACE_LEFT = 15
BRACE_RIGHT = 16
ASSIGNMENT = 17
STRUCT = 18
STATIC = 19
SQUARE_BRACKET_LEFT = 20
SQUARE_BRACKET_RIGHT = 21
COLON = 22
VOID = 23
ASTERISK = 24
ADDITION = 25
SUBTRACTION = 26
INCREMENT = 27
DECREMENT = 28
DIVISION = 29
MODULO = 30
EQUAL_TO = 31
NOT_EQUAL_TO = 32
LESS_THAN = 33
GREATER_THAN = 34
LESS_OR_EQUAL = 35
GREATER_OR_EQUAL = 36
NOT = 37
LOGICAL_END = 38
LOGICAL_OR = 39
BITWISE_NOT = 40
BITWISE_AND = 41
BITWISE_OR = 42
BITWISE_XOR = 43
BITWISE_LEFT_SHIFT = 44
BITWISE_RIGHT_SHIFT = 45
ADDITION_ASSIGNMENT = 46
SUBTRACTION_ASSIGNMENT = 47
MULTIPLICATION_ASSIGNMENT = 48
DIVISION_ASSIGNMENT = 49
MODULO_ASSIGNMENT = 50
BITWISE_AND_ASSIGNMENT = 51
BITWISE_OR_ASSIGNMENT = 52
BITWISE_XOR_ASSIGNMENT = 53
BITWISE_L_SHIFT_ASSIGNMENT = 54
BITWISE_R_SHIFT_ASSIGNMENT = 55
STRUCTURE_DEREFERENCE = 56
QUESTION_MARK = 57
SIZEOF = 58
ALIGNOF = 59
SINGLE_LINE_COMMENT = 60


class directivesDict(dict):
    def __init__(self):
        self['include'] = INCLUDE
        # by default we always interpret definition as an object-like macros
        self['define'] = OBJECT_LIKE_MACRO


class keyWordsDict(dict):
    def __init__(self):
        self['typedef'] = TYPEDEF
        self['enum'] = ENUM
        self['...'] = VARIADIC_ARGS
        self['struct'] = STRUCT
        self['static'] = STATIC
        self['void'] = VOID
        self['sizeof'] = SIZEOF
        self['alignof'] = ALIGNOF


class singlePunctuatorDict(dict):
    def __init__(self):
        self['+'] = ADDITION
        self['-'] = SUBTRACTION
        self['='] = ASSIGNMENT
        self['!'] = NOT
        self['<'] = LESS_THAN
        self['>'] = GREATER_THAN
        self['~'] = BITWISE_NOT
        self['&'] = BITWISE_AND
        self['|'] = BITWISE_OR
        self['^'] = BITWISE_XOR
        self['*'] = ASTERISK
        self['/'] = DIVISION
        self['%'] = MODULO
        self['?'] = QUESTION_MARK


class pairPunctuatorDict(dict):
    def __init__(self):
        self['++'] = INCREMENT
        self['--'] = DECREMENT
        self['!='] = NOT_EQUAL_TO
        self['=='] = EQUAL_TO
        self['<='] = LESS_OR_EQUAL
        self['>='] = GREATER_OR_EQUAL
        self['&&'] = LOGICAL_END
        self['||'] = LOGICAL_OR
        self['<<'] = BITWISE_LEFT_SHIFT
        self['>>'] = BITWISE_RIGHT_SHIFT
        self['+='] = ADDITION_ASSIGNMENT
        self['-='] = SUBTRACTION_ASSIGNMENT
        self['*='] = MULTIPLICATION_ASSIGNMENT
        self['/='] = DIVISION_ASSIGNMENT
        self['%='] = MODULO_ASSIGNMENT
        self['&='] = BITWISE_AND_ASSIGNMENT
        self['|='] = BITWISE_OR_ASSIGNMENT
        self['^='] = BITWISE_XOR_ASSIGNMENT
        self['->'] = STRUCTURE_DEREFERENCE
        self['//'] = SINGLE_LINE_COMMENT


class triplePunctuatorDict(dict):
    def __init__(self):
        self['<<='] = BITWISE_L_SHIFT_ASSIGNMENT
        self['>>='] = BITWISE_R_SHIFT_ASSIGNMENT