__author__ = 'V8q1ez'

from collections import deque

class Grammar():
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
    MULTI_LINE_COMMENT_START = 61
    MULTI_LINE_COMMENT_LINE = 62
    MULTI_LINE_COMMENT_END = 63
    HASH = 64

    def __init__(self):
        self._directives = {}
        self._directives['include'] = self.INCLUDE
        # by default we always interpret definition as an object-like macros
        self._directives['define'] = self.OBJECT_LIKE_MACRO

        self._keyWords = {}
        self._keyWords['typedef'] = self.TYPEDEF
        self._keyWords['enum'] = self.ENUM
        self._keyWords['...'] = self.VARIADIC_ARGS
        self._keyWords['struct'] = self.STRUCT
        self._keyWords['static'] = self.STATIC
        self._keyWords['void'] = self.VOID
        self._keyWords['sizeof'] = self.SIZEOF
        self._keyWords['alignof'] = self.ALIGNOF

        self._singlePunctuators = {}
        self._singlePunctuators['+'] = self.ADDITION
        self._singlePunctuators['-'] = self.SUBTRACTION
        self._singlePunctuators['='] = self.ASSIGNMENT
        self._singlePunctuators['!'] = self.NOT
        self._singlePunctuators['<'] = self.LESS_THAN
        self._singlePunctuators['>'] = self.GREATER_THAN
        self._singlePunctuators['~'] = self.BITWISE_NOT
        self._singlePunctuators['&'] = self.BITWISE_AND
        self._singlePunctuators['|'] = self.BITWISE_OR
        self._singlePunctuators['^'] = self.BITWISE_XOR
        self._singlePunctuators['*'] = self.ASTERISK
        self._singlePunctuators['/'] = self.DIVISION
        self._singlePunctuators['%'] = self.MODULO
        self._singlePunctuators['?'] = self.QUESTION_MARK
        self._singlePunctuators[':'] = self.COLON
        self._singlePunctuators[';'] = self.SEMICOLON
        self._singlePunctuators['['] = self.SQUARE_BRACKET_LEFT
        self._singlePunctuators[']'] = self.SQUARE_BRACKET_RIGHT
        self._singlePunctuators['{'] = self.BRACE_LEFT
        self._singlePunctuators['}'] = self.BRACE_RIGHT
        self._singlePunctuators[','] = self.COMMA
        self._singlePunctuators['#'] = self.HASH
        self._singlePunctuators[')'] = self.PARENTHESIS_RIGHT

        self._pairPunctuators = {}
        self._pairPunctuators['++'] = self.INCREMENT
        self._pairPunctuators['--'] = self.DECREMENT
        self._pairPunctuators['!='] = self.NOT_EQUAL_TO
        self._pairPunctuators['=='] = self.EQUAL_TO
        self._pairPunctuators['<='] = self.LESS_OR_EQUAL
        self._pairPunctuators['>='] = self.GREATER_OR_EQUAL
        self._pairPunctuators['&&'] = self.LOGICAL_END
        self._pairPunctuators['||'] = self.LOGICAL_OR
        self._pairPunctuators['<<'] = self.BITWISE_LEFT_SHIFT
        self._pairPunctuators['>>'] = self.BITWISE_RIGHT_SHIFT
        self._pairPunctuators['+='] = self.ADDITION_ASSIGNMENT
        self._pairPunctuators['-='] = self.SUBTRACTION_ASSIGNMENT
        self._pairPunctuators['*='] = self.MULTIPLICATION_ASSIGNMENT
        self._pairPunctuators['/='] = self.DIVISION_ASSIGNMENT
        self._pairPunctuators['%='] = self.MODULO_ASSIGNMENT
        self._pairPunctuators['&='] = self.BITWISE_AND_ASSIGNMENT
        self._pairPunctuators['|='] = self.BITWISE_OR_ASSIGNMENT
        self._pairPunctuators['^='] = self.BITWISE_XOR_ASSIGNMENT
        self._pairPunctuators['->'] = self.STRUCTURE_DEREFERENCE
        self._pairPunctuators['//'] = self.SINGLE_LINE_COMMENT
        self._pairPunctuators['/*'] = self.MULTI_LINE_COMMENT_START
        self._pairPunctuators['*/'] = self.MULTI_LINE_COMMENT_END

        self._triplePunctuators = {}
        self._triplePunctuators['<<='] = self.BITWISE_L_SHIFT_ASSIGNMENT
        self._triplePunctuators['>>='] = self.BITWISE_R_SHIFT_ASSIGNMENT

    def isItSinglePunctuator(self, character):
        return character in self._singlePunctuators

    def isItPairPunctuator(self, twoCharacters):
        return twoCharacters in self._pairPunctuators

    def isItTriplePunctuator(self, threeCharacters):
        return threeCharacters in self._triplePunctuators

    def getSinglePunctuatorByCharacter(self, character):
        return self._singlePunctuators[character]

    def getPairPunctuatorByCharacter(self, twoCharacters):
        return self._pairPunctuators[twoCharacters]

    def getTriplePunctuatorByCharacter(self, threeCharacters):
        return self._triplePunctuators[threeCharacters]

    def isItKeyWord(self, literal):
        return literal in self._keyWords

    def getKeyWordByLiteral(self, literal):
        return self._keyWords[literal]

    def isItDirective(self, literal):
        return literal in self._directives

    def getDirectiveByLiteral(self, literal):
        return self._directives[literal]



class token():
    def __init__(self, type):
        self.type = type
        self.literalValue = ''



class CCodeParser():
    def __init__(self, grammar):
        self._tokensList = []
        self._punctuatorsCache = deque()

        self._characterHandlersDict = {
            '(' : self._processLeftParenthesis,
            '"' : self._processQuote,
            ' ' : self._processSpace,
            }
        self._grammar = grammar

    def _clearState(self):
        self.isLiteralStarted = False
        self.isStringStarted = False
        self.isEscSeqStarted = False
        self.isNameOfMacrosNeeded = False
        self.literalValue = ''
        self.isDirectiveStarted = False
        self.isSingleLineCommentStarted = False
        self.isMultiLineCommentStarted = False
        self.isNameOfMacrosNeeded = False

    def _addSimpleToken(self, tokenType):
        self._tokensList.append( token(tokenType) )

    def _addLiteralToken(self, literalValue):
        t = token(self._grammar.LITERAL)
        t.literalValue = literalValue
        self._tokensList.append(t)

    def _addStringToken(self, literalValue):
        t = token(self._grammar.STRING)
        t.literalValue = literalValue
        self._tokensList.append(t)

    def _addSingleLineCommentToken(self, literalValue):
        t = token(self._grammar.SINGLE_LINE_COMMENT)
        t.literalValue = literalValue
        self._tokensList.append(t)

    def _addMultiLineCommentLineToken(self, literalValue):
        t = token(self._grammar.MULTI_LINE_COMMENT_LINE)
        t.literalValue = literalValue
        self._tokensList.append(t)

    """
    All used preprocessor rules are taken from:
        https://gcc.gnu.org/onlinedocs/cpp/index.html
    """

    def _parseLine(self, remainingString):

        for c in remainingString:

            if self.isSingleLineCommentStarted:
                self.literalValue += c
                continue

            elif c == '\\':
                if not self.isEscSeqStarted:
                    self.isEscSeqStarted = True
                    continue

            self._tryToCompletePreviousToken( c )

            if self._grammar.isItSinglePunctuator(c):
                if self.isStringStarted:
                    self.literalValue += c
                else:
                    if self.isLiteralStarted:
                        self._processFoundLiteral()

            elif c in self._characterHandlersDict:
                handlerToCall = self._characterHandlersDict[ c ]
                handlerToCall()

            elif c != ' ':
                self._processNonSpace( c )

        self._processEndOfLine()

        return

    def _processLeftParenthesis(self):
        if self.isNameOfMacrosNeeded:
          self._addSimpleToken(self._grammar.FUNCTION_LIKE_MACRO)
          self._addLiteralToken(self.literalValue)
          self.isNameOfMacrosNeeded = False
          self._addSimpleToken(self._grammar.PARENTHESIS_LEFT)

        elif self.isStringStarted:
            self.literalValue += '('
        else:
            if self.isLiteralStarted:
                # if not self.isNameOfMacrosNeeded:
                    # There is no space between name and parenthesis
                    # So we should change the type of first token
                    # self._tokensList.changeTokenType( 0, FUNCTION_LIKE_MACRO )
                    # self.isNameOfMacrosNeeded = True
                    # and write the macros name
                self._processFoundLiteral()
            self._addSimpleToken(self._grammar.PARENTHESIS_LEFT)

        return


    def _processQuote(self):
        if self.isStringStarted:
            if self.isEscSeqStarted:
                self.literalValue += '\\\"'
                self.isEscSeqStarted = False
            else:
                self._addStringToken(self.literalValue)
                self.isStringStarted = False
                self._addSimpleToken(self._grammar.QUOTE)
        else:
            if self.isLiteralStarted:
                self._processFoundLiteral()
            else:
                self.literalValue = ''
                self.isStringStarted = True
            self._addSimpleToken(self._grammar.QUOTE)

        return

    def _processSpace(self):
        if self.isDirectiveStarted:
            self._processFoundDirective()
        elif self.isNameOfMacrosNeeded:
            self._lastFoundMacrosName = self.literalValue
            self.isNameOfMacrosNeeded = False
            self._addSimpleToken(self._grammar.OBJECT_LIKE_MACRO)
            self._addLiteralToken(self.literalValue)
        elif self.isStringStarted \
                or self.isSingleLineCommentStarted\
                or self.isMultiLineCommentStarted:
            self.literalValue += ' '
        elif self.isLiteralStarted:
            self._processFoundLiteral()
        return

    def _processNonSpace(self, c):
        if self.isDirectiveStarted or self.isNameOfMacrosNeeded:
            self.literalValue += c
        elif self.isStringStarted:
            if self.isEscSeqStarted:
                self.literalValue += '\\'
                self.isEscSeqStarted = False
            self.literalValue += c
        else:
            if self.isSingleLineCommentStarted or self.isMultiLineCommentStarted:
                self.literalValue += c
            elif not self.isLiteralStarted:
                self.literalValue = c
                self.isLiteralStarted = True
            else:
                self.literalValue += c
        return

    def _processFoundDirective(self):
        if self._grammar.isItDirective(self.literalValue):
            self.isDirectiveStarted = False
            if self.literalValue == 'define':
                self.isNameOfMacrosNeeded = True
            else:
                self._addSimpleToken(self._grammar.getDirectiveByLiteral(self.literalValue))
        else:
            self._addSimpleToken(self._grammar.UNKNOWN)
        self.literalValue = ''
        return

    def _processFoundLiteral(self):
        if self._grammar.isItKeyWord(self.literalValue):
            self._addSimpleToken(self._grammar.getKeyWordByLiteral(self.literalValue))
        else:
            self._addLiteralToken(self.literalValue)
        self.isLiteralStarted = False
        return

    def _tryToCompletePreviousToken(self, c):
        if not self.isStringStarted:
            if self._grammar.isItSinglePunctuator(c):
                self._punctuatorsCache.append(c)
            else:
                self._processCachedPunctuators()

        return

    def _processCachedPunctuators(self):
        punctuator = self._grammar.UNKNOWN
        while len(self._punctuatorsCache):

            if self.isSingleLineCommentStarted:
                self.literalValue += self._punctuatorsCache.popleft()

            elif self.isMultiLineCommentStarted:
                # only MULTI_LINE_COMMENT_END of EOL are allowed
                if len(self._punctuatorsCache) >= 2:
                    firstTwoChars = ''.join(list(self._punctuatorsCache)[0:2])
                    if self._grammar.isItPairPunctuator(firstTwoChars):
                        punctuator = self._grammar.getPairPunctuatorByCharacter(firstTwoChars)
                    if punctuator == self._grammar.MULTI_LINE_COMMENT_END:
                        for _ in range(2):
                            self._punctuatorsCache.popleft()
                        self.isMultiLineCommentStarted = False
                        self._addMultiLineCommentLineToken(self.literalValue)
                        self._addSimpleToken(punctuator)
                    else:
                        self.literalValue += self._punctuatorsCache.popleft()
                else:
                    self.literalValue += self._punctuatorsCache.popleft()
            else:
                if len(self._punctuatorsCache) >= 3:
                    lastThreeChars = ''.join(list(self._punctuatorsCache)[0:3])
                    firstTwoChars = ''.join(list(self._punctuatorsCache)[0:2])
                    char = ''.join(list(self._punctuatorsCache)[0:1])
                    if self._grammar.isItTriplePunctuator(lastThreeChars):
                        punctuator = self._grammar.getTriplePunctuatorByCharacter(lastThreeChars)
                        for _ in range(3):
                            self._punctuatorsCache.popleft()
                    elif self._grammar.isItPairPunctuator(firstTwoChars):
                        punctuator = self._grammar.getPairPunctuatorByCharacter(firstTwoChars)
                        for _ in range(2):
                            self._punctuatorsCache.popleft()
                    elif self._grammar.isItSinglePunctuator(char):
                        punctuator = self._grammar.getSinglePunctuatorByCharacter(char)
                        for _ in range(1):
                            self._punctuatorsCache.popleft()

                elif len(self._punctuatorsCache) == 2:
                    firstTwoChars = ''.join(list(self._punctuatorsCache)[0:2])
                    char = ''.join(list(self._punctuatorsCache)[0:1])
                    if self._grammar.isItPairPunctuator(firstTwoChars):
                        punctuator = self._grammar.getPairPunctuatorByCharacter(firstTwoChars)
                        for _ in range(2):
                            self._punctuatorsCache.popleft()
                    elif self._grammar.isItSinglePunctuator(char):
                        punctuator = self._grammar.getSinglePunctuatorByCharacter(char)
                        for _ in range(1):
                            self._punctuatorsCache.popleft()

                elif len(self._punctuatorsCache) == 1:
                    char = ''.join(list(self._punctuatorsCache)[0:1])
                    if self._grammar.isItSinglePunctuator(char):
                        punctuator = self._grammar.getSinglePunctuatorByCharacter(char)
                        for _ in range(1):
                            self._punctuatorsCache.popleft()

                if punctuator != self._grammar.UNKNOWN:
                    if punctuator == self._grammar.SINGLE_LINE_COMMENT:
                        self.isSingleLineCommentStarted = True
                        self.literalValue = ''
                    elif punctuator == self._grammar.HASH:
                        if not self.isStringStarted and not self.isDirectiveStarted:
                            self.literalValue = ''
                            self.isDirectiveStarted = True
                            self.isNameOfMacrosNeeded = False
                    else:
                        if punctuator == self._grammar.MULTI_LINE_COMMENT_START:
                            self.isMultiLineCommentStarted = True
                            self.literalValue = ''
                        elif punctuator == self._grammar.MULTI_LINE_COMMENT_END:
                            self.isMultiLineCommentStarted = False
                            self._addMultiLineCommentLineToken(self.literalValue)

                        self._addSimpleToken(punctuator)

                    punctuator = self._grammar.UNKNOWN

        self._punctuatorsCache.clear()

        return

    def _processEndOfLine(self):
        if self.isEscSeqStarted:
            if self.isLiteralStarted:
                pass
                #self._tokensList.addLiteralToken( self.literalValue )
                #self.isLiteralStarted = False
            # esc sequence cannot be between two lines
            self.isEscSeqStarted = False
        else:
            if self.isSingleLineCommentStarted:
                self._addSingleLineCommentToken(self.literalValue)
                self.isSingleLineCommentStarted = False

            elif self.isLiteralStarted:
                self._processFoundLiteral()
            elif self.isDirectiveStarted:
                self._processFoundDirective()
            elif self.isNameOfMacrosNeeded:
                self._lastFoundMacrosName = self.literalValue
                self.isNameOfMacrosNeeded = False
                self._addSimpleToken(self._grammar.OBJECT_LIKE_MACRO)
                self._addLiteralToken(self.literalValue)
            else:
                self._processCachedPunctuators()
                if self.isMultiLineCommentStarted:
                    self._addMultiLineCommentLineToken(self.literalValue)
                    self.literalValue = ''
            self._addSimpleToken(self._grammar.EOL)

        return

    def parseText(self, text):
        self._clearState()
        for line in text:
            self._parseLine(line)

        if self.isLiteralStarted:
            self._addLiteralToken(self.literalValue)

        return self._tokensList