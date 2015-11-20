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


class CCodeParsingContext():
    def __init__(self):
        self.tokensList = []
        self.isLiteralStarted = False
        self.isStringStarted = False
        self.isEscSeqStarted = False
        self.isNameOfMacrosNeeded = False
        self.literalValue = ''
        self.isDirectiveStarted = False
        self.isSingleLineCommentStarted = False
        self.isMultiLineCommentStarted = False
        self.isNameOfMacrosNeeded = False
        self.punctuatorsCache = deque()

    def clearState(self):
        self.isLiteralStarted = False
        self.isStringStarted = False
        self.isEscSeqStarted = False
        self.isNameOfMacrosNeeded = False
        self.literalValue = ''
        self.isDirectiveStarted = False
        self.isSingleLineCommentStarted = False
        self.isMultiLineCommentStarted = False
        self.isNameOfMacrosNeeded = False

    def addSimpleToken(self, tokenType):
        self.tokensList.append( token(tokenType) )

    def addLiteralToken(self, literalValue):
        t = token(Grammar.LITERAL)
        t.literalValue = literalValue
        self.tokensList.append(t)

    def addStringToken(self, literalValue):
        t = token(Grammar.STRING)
        t.literalValue = literalValue
        self.tokensList.append(t)

    def addSingleLineCommentToken(self, literalValue):
        t = token(Grammar.SINGLE_LINE_COMMENT)
        t.literalValue = literalValue
        self.tokensList.append(t)

    def addMultiLineCommentLineToken(self, literalValue):
        t = token(Grammar.MULTI_LINE_COMMENT_LINE)
        t.literalValue = literalValue
        self.tokensList.append(t)



class CCodeParser():
    def __init__(self, grammar):

        self._characterHandlersDict = {
            '(' : self._processLeftParenthesis,
            '"' : self._processQuote,
            ' ' : self._processSpace,
            }
        self._grammar = grammar

    """
    All used preprocessor rules are taken from:
        https://gcc.gnu.org/onlinedocs/cpp/index.html
    """

    def _parseLine(self, remainingString, parsingContext):

        for c in remainingString:

            if parsingContext.isSingleLineCommentStarted:
                parsingContext.literalValue += c
                continue

            elif c == '\\':
                if not parsingContext.isEscSeqStarted:
                    parsingContext.isEscSeqStarted = True
                    continue

            self._tryToCompletePreviousToken( c, parsingContext )

            if self._grammar.isItSinglePunctuator(c):
                if parsingContext.isStringStarted:
                    parsingContext.literalValue += c
                else:
                    if parsingContext.isLiteralStarted:
                        self._processFoundLiteral(parsingContext)

            elif c in self._characterHandlersDict:
                handlerToCall = self._characterHandlersDict[ c ]
                handlerToCall(parsingContext)

            elif c != ' ':
                self._processNonSpace( c, parsingContext )

        self._processEndOfLine(parsingContext)

        return

    def _processLeftParenthesis(self, parsingContext):
        if parsingContext.isNameOfMacrosNeeded:
          parsingContext.addSimpleToken(Grammar.FUNCTION_LIKE_MACRO)
          parsingContext.addLiteralToken(parsingContext.literalValue)
          parsingContext.isNameOfMacrosNeeded = False
          parsingContext.addSimpleToken(Grammar.PARENTHESIS_LEFT)

        elif parsingContext.isStringStarted:
            parsingContext.literalValue += '('
        else:
            if parsingContext.isLiteralStarted:
                # if not self.isNameOfMacrosNeeded:
                    # There is no space between name and parenthesis
                    # So we should change the type of first token
                    # self._tokensList.changeTokenType( 0, FUNCTION_LIKE_MACRO )
                    # self.isNameOfMacrosNeeded = True
                    # and write the macros name
                self._processFoundLiteral(parsingContext)
            parsingContext.addSimpleToken(Grammar.PARENTHESIS_LEFT)

        return


    def _processQuote(self, parsingContext):
        if parsingContext.isStringStarted:
            if parsingContext.isEscSeqStarted:
                parsingContext.literalValue += '\\\"'
                parsingContext.isEscSeqStarted = False
            else:
                parsingContext.addStringToken(parsingContext.literalValue)
                parsingContext.isStringStarted = False
                parsingContext.addSimpleToken(Grammar.QUOTE)
        else:
            if parsingContext.isLiteralStarted:
                self._processFoundLiteral(parsingContext)
            else:
                parsingContext.literalValue = ''
                parsingContext.isStringStarted = True
            parsingContext.addSimpleToken(Grammar.QUOTE)

        return

    def _processSpace(self, parsingContext):
        if parsingContext.isDirectiveStarted:
            self._processFoundDirective(parsingContext)
        elif parsingContext.isNameOfMacrosNeeded:
            # self._lastFoundMacrosName = parsingContext.literalValue
            parsingContext.isNameOfMacrosNeeded = False
            parsingContext.addSimpleToken(Grammar.OBJECT_LIKE_MACRO)
            parsingContext.addLiteralToken(parsingContext.literalValue)
        elif parsingContext.isStringStarted \
                or parsingContext.isSingleLineCommentStarted\
                or parsingContext.isMultiLineCommentStarted:
            parsingContext.literalValue += ' '
        elif parsingContext.isLiteralStarted:
            self._processFoundLiteral(parsingContext)
        return

    def _processNonSpace(self, c, parsingContext):
        if parsingContext.isDirectiveStarted or parsingContext.isNameOfMacrosNeeded:
            parsingContext.literalValue += c
        elif parsingContext.isStringStarted:
            if parsingContext.isEscSeqStarted:
                parsingContext.literalValue += '\\'
                parsingContext.isEscSeqStarted = False
            parsingContext.literalValue += c
        else:
            if parsingContext.isSingleLineCommentStarted or parsingContext.isMultiLineCommentStarted:
                parsingContext.literalValue += c
            elif not parsingContext.isLiteralStarted:
                parsingContext.literalValue = c
                parsingContext.isLiteralStarted = True
            else:
                parsingContext.literalValue += c
        return

    def _processFoundDirective(self, parsingContext):
        if self._grammar.isItDirective(parsingContext.literalValue):
            parsingContext.isDirectiveStarted = False
            if parsingContext.literalValue == 'define':
                parsingContext.isNameOfMacrosNeeded = True
            else:
                parsingContext.addSimpleToken(self._grammar.getDirectiveByLiteral(parsingContext.literalValue))
        else:
            parsingContext.addSimpleToken(Grammar.UNKNOWN)
        parsingContext.literalValue = ''
        return

    def _processFoundLiteral(self, parsingContext):
        if self._grammar.isItKeyWord(parsingContext.literalValue):
            parsingContext.addSimpleToken(self._grammar.getKeyWordByLiteral(parsingContext.literalValue))
        else:
            parsingContext.addLiteralToken(parsingContext.literalValue)
        parsingContext.isLiteralStarted = False
        return

    def _tryToCompletePreviousToken(self, c, parsingContext):
        if not parsingContext.isStringStarted:
            if self._grammar.isItSinglePunctuator(c):
                parsingContext.punctuatorsCache.append(c)
            else:
                self._processCachedPunctuators(parsingContext)

        return

    def _processCachedPunctuators(self, parsingContext):
        punctuator = Grammar.UNKNOWN
        while len(parsingContext.punctuatorsCache):

            if parsingContext.isSingleLineCommentStarted:
                parsingContext.literalValue += parsingContext.punctuatorsCache.popleft()

            elif parsingContext.isMultiLineCommentStarted:
                # only MULTI_LINE_COMMENT_END of EOL are allowed
                if len(parsingContext.punctuatorsCache) >= 2:
                    firstTwoChars = ''.join(list(parsingContext.punctuatorsCache)[0:2])
                    if self._grammar.isItPairPunctuator(firstTwoChars):
                        punctuator = self._grammar.getPairPunctuatorByCharacter(firstTwoChars)
                    if punctuator == Grammar.MULTI_LINE_COMMENT_END:
                        for _ in range(2):
                            parsingContext.punctuatorsCache.popleft()
                        parsingContext.isMultiLineCommentStarted = False
                        parsingContext.addMultiLineCommentLineToken(parsingContext.literalValue)
                        parsingContext.addSimpleToken(punctuator)
                    else:
                        parsingContext.literalValue += parsingContext.punctuatorsCache.popleft()
                else:
                    parsingContext.literalValue += parsingContext.punctuatorsCache.popleft()
            else:
                if len(parsingContext.punctuatorsCache) >= 3:
                    lastThreeChars = ''.join(list(parsingContext.punctuatorsCache)[0:3])
                    firstTwoChars = ''.join(list(parsingContext.punctuatorsCache)[0:2])
                    char = ''.join(list(parsingContext.punctuatorsCache)[0:1])
                    if self._grammar.isItTriplePunctuator(lastThreeChars):
                        punctuator = self._grammar.getTriplePunctuatorByCharacter(lastThreeChars)
                        for _ in range(3):
                            parsingContext.punctuatorsCache.popleft()
                    elif self._grammar.isItPairPunctuator(firstTwoChars):
                        punctuator = self._grammar.getPairPunctuatorByCharacter(firstTwoChars)
                        for _ in range(2):
                            parsingContext.punctuatorsCache.popleft()
                    elif self._grammar.isItSinglePunctuator(char):
                        punctuator = self._grammar.getSinglePunctuatorByCharacter(char)
                        for _ in range(1):
                            parsingContext.punctuatorsCache.popleft()

                elif len(parsingContext.punctuatorsCache) == 2:
                    firstTwoChars = ''.join(list(parsingContext.punctuatorsCache)[0:2])
                    char = ''.join(list(parsingContext.punctuatorsCache)[0:1])
                    if self._grammar.isItPairPunctuator(firstTwoChars):
                        punctuator = self._grammar.getPairPunctuatorByCharacter(firstTwoChars)
                        for _ in range(2):
                            parsingContext.punctuatorsCache.popleft()
                    elif self._grammar.isItSinglePunctuator(char):
                        punctuator = self._grammar.getSinglePunctuatorByCharacter(char)
                        for _ in range(1):
                            parsingContext.punctuatorsCache.popleft()

                elif len(parsingContext.punctuatorsCache) == 1:
                    char = ''.join(list(parsingContext.punctuatorsCache)[0:1])
                    if self._grammar.isItSinglePunctuator(char):
                        punctuator = self._grammar.getSinglePunctuatorByCharacter(char)
                        for _ in range(1):
                            parsingContext.punctuatorsCache.popleft()

                if punctuator != Grammar.UNKNOWN:
                    if punctuator == Grammar.SINGLE_LINE_COMMENT:
                        parsingContext.isSingleLineCommentStarted = True
                        parsingContext.literalValue = ''
                    elif punctuator == Grammar.HASH:
                        if not parsingContext.isStringStarted and not parsingContext.isDirectiveStarted:
                            parsingContext.literalValue = ''
                            parsingContext.isDirectiveStarted = True
                            parsingContext.isNameOfMacrosNeeded = False
                    else:
                        if punctuator == Grammar.MULTI_LINE_COMMENT_START:
                            parsingContext.isMultiLineCommentStarted = True
                            parsingContext.literalValue = ''
                        elif punctuator == Grammar.MULTI_LINE_COMMENT_END:
                            parsingContext.isMultiLineCommentStarted = False
                            parsingContext.addMultiLineCommentLineToken(parsingContext.literalValue)

                        parsingContext.addSimpleToken(punctuator)

                    punctuator = Grammar.UNKNOWN

        parsingContext.punctuatorsCache.clear()

        return

    def _processEndOfLine(self, parsingContext):
        if parsingContext.isEscSeqStarted:
            if parsingContext.isLiteralStarted:
                pass
                #self._tokensList.addLiteralToken( self.literalValue )
                #self.isLiteralStarted = False
            # esc sequence cannot be between two lines
            parsingContext.isEscSeqStarted = False
        else:
            if parsingContext.isSingleLineCommentStarted:
                parsingContext.addSingleLineCommentToken(parsingContext.literalValue)
                parsingContext.isSingleLineCommentStarted = False

            elif parsingContext.isLiteralStarted:
                self._processFoundLiteral(parsingContext)
            elif parsingContext.isDirectiveStarted:
                self._processFoundDirective(parsingContext)
            elif parsingContext.isNameOfMacrosNeeded:
                # parsingContext._lastFoundMacrosName = parsingContext.literalValue
                parsingContext.isNameOfMacrosNeeded = False
                parsingContext.addSimpleToken(Grammar.OBJECT_LIKE_MACRO)
                parsingContext.addLiteralToken(parsingContext.literalValue)
            else:
                self._processCachedPunctuators(parsingContext)
                if parsingContext.isMultiLineCommentStarted:
                    parsingContext.addMultiLineCommentLineToken(parsingContext.literalValue)
                    parsingContext.literalValue = ''
            parsingContext.addSimpleToken(Grammar.EOL)

        return

    def parseText(self, text, parsingContext):
        parsingContext.clearState()
        for line in text:
            self._parseLine(line, parsingContext)

        if parsingContext.isLiteralStarted:
            parsingContext.addLiteralToken(parsingContext.literalValue)

        return parsingContext.tokensList