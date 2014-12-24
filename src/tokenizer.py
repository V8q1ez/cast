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
STAR = 24
ADDITION = 25
SUBTRACTION = 26
INCREMENT = 27
DECREMENT = 28


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


class token():
    def __init__(self, type):
        self.type = type
        self.literalValue = ''


class tokenList():
    def __init__(self):
        self.tokensList = []

    def addSimpleToken(self, tokenType):
        self.tokensList.append( token(tokenType) )

    def addLiteralToken(self, literalValue):
        t = token(LITERAL)
        t.literalValue = literalValue
        self.tokensList.append(t)

    def addStringToken(self, literalValue):
        t = token(STRING)
        t.literalValue = literalValue
        self.tokensList.append(t)

    def changeTokenType(self, index, newType):
        self.tokensList[ index ].type = newType

    def getList(self):
        return self.tokensList


class tokenizer():
    def __init__(self):
        self._tokensList = tokenList()
        self.knownDirectives = directivesDict()
        self._knownKeywords = keyWordsDict()
        self._characterHandlersDict = {
            '(' : self._processLeftParenthesis,
            ')' : self._processRightParenthesis,
            '{' : self._processLeftBrace,
            '}' : self._processRightBrace,
            ',' : self._processComma,
            ';' : self._processSemicolon,
            ':' : self._processColon,
            '"' : self._processQuote,
            '#' : self._processSharp,
            '*' : self._processStar,
            '+' : self._processPlus,
            '-' : self._processMinus,
            '=' : self._processEqual,
            '[' : self._processSquareBracketLeft,
            ']' : self._processSquareBracketRight,
            ' ' : self._processSpace
            }

    def _clearState(self):
        self.isLiteralStarted = False
        self.isStringStarted = False
        self.isEscSeqStarted = False
        self.isTypeOfMacrosKnown = False
        self.literalValue = ''
        self.isDirectiveStarted = False
        self._previousCharacter = ''
        self.isPunctuatorComplete = False

    """
    All used preprocessor rules are taken from:
        https://gcc.gnu.org/onlinedocs/cpp/index.html
    """

    def parseDefine(self, remainingString):

        self._previousCharacter = ''

        for c in remainingString:

            self._tryToCompletePreviousToken( c )

            if c in self._characterHandlersDict:
                handlerToCall = self._characterHandlersDict[ c ]
                handlerToCall()

            elif c == '\\':
                if not self.isEscSeqStarted:
                    self.isEscSeqStarted = True

            elif c != ' ':
                self._processNonSpace( c )

            self._previousCharacter = c

        self._processEndOfLine()

        return

    def _processLeftParenthesis(self):
        if self.isStringStarted:
            self.literalValue += '('
        else:
            if self.isLiteralStarted:
                if not self.isTypeOfMacrosKnown:
                    # There is no space between name and parenthesis
                    # So we should change the type of first token
                    self._tokensList.changeTokenType( 0, FUNCTION_LIKE_MACRO )
                    self.isTypeOfMacrosKnown = True
                    # and write the macros name
                self._processFoundLiteral()
            self._tokensList.addSimpleToken( PARENTHESIS_LEFT )

        return

    def _processRightParenthesis(self):
        if self.isStringStarted:
            self.literalValue += ')'
        else:
            if self.isLiteralStarted:
                self._processFoundLiteral()
            self._tokensList.addSimpleToken( PARENTHESIS_RIGHT )
        return

    def _processLeftBrace(self):
        if self.isStringStarted:
            self.literalValue += '{'
        else:
            if self.isLiteralStarted:
                self._processFoundLiteral()
            self._tokensList.addSimpleToken( BRACE_LEFT )
        return

    def _processRightBrace(self):
        if self.isStringStarted:
            self.literalValue += '}'
        else:
            if self.isLiteralStarted:
                self._processFoundLiteral()
            self._tokensList.addSimpleToken( BRACE_RIGHT )
        return

    def _processSquareBracketLeft(self):
        if self.isStringStarted:
            self.literalValue += '['
        else:
            if self.isLiteralStarted:
                self._processFoundLiteral()
            self._tokensList.addSimpleToken( SQUARE_BRACKET_LEFT )
        return

    def _processSquareBracketRight(self):
        if self.isStringStarted:
            self.literalValue += ']'
        else:
            if self.isLiteralStarted:
                self._processFoundLiteral()
            self._tokensList.addSimpleToken( SQUARE_BRACKET_RIGHT )
        return

    def _processComma(self):
        if self.isStringStarted:
            self.literalValue +=','
        else:
            if self.isLiteralStarted:
                self._processFoundLiteral()
            self._tokensList.addSimpleToken( COMMA )
        return

    def _processSemicolon(self):
        if self.isStringStarted:
            self.literalValue += ';'
        else:
            if self.isLiteralStarted:
                self._processFoundLiteral()
            self._tokensList.addSimpleToken( SEMICOLON )
        return

    def _processColon(self):
        if self.isStringStarted:
            self.literalValue += ':'
        else:
            if self.isLiteralStarted:
                self._processFoundLiteral()
            self._tokensList.addSimpleToken( COLON )
        return

    def _processQuote(self):
        if self.isStringStarted:
            if self.isEscSeqStarted:
                self.literalValue += '\\\"'
                self.isEscSeqStarted = False
            else:
                self._tokensList.addStringToken( self.literalValue )
                self.isStringStarted = False
                self._tokensList.addSimpleToken( QUOTE )
        else:
            if self.isLiteralStarted:
                self._tokensList.addLiteralToken( self.literalValue )
                self.isLiteralStarted = False
            else:
                self.literalValue = ''
                self.isStringStarted = True
            self._tokensList.addSimpleToken( QUOTE )

        return

    def _processSpace(self):
        if self.isDirectiveStarted:
            self._processFoundDirective()
        elif self.isStringStarted:
            self.literalValue += ' '
        elif self.isLiteralStarted:
            # since literal finishes by space - this is an object like macros
            self.isTypeOfMacrosKnown = True
            self._processFoundLiteral()
        return

    def _processNonSpace(self, c):
        if self.isDirectiveStarted:
            self.literalValue += c
        elif self.isStringStarted:
            if self.isEscSeqStarted:
                self.literalValue += '\\'
                self.isEscSeqStarted = False
            self.literalValue += c
        else:
            if not self.isLiteralStarted:
                self.literalValue = c
                self.isLiteralStarted = True
            else:
                self.literalValue += c
        return

    def _processSharp(self):
        if self.isStringStarted:
            self.literalValue += '#'
        else:
            if not self.isDirectiveStarted:
                self.literalValue = ''
                self.isDirectiveStarted = True
        return

    def _processStar(self):
        if self.isStringStarted:
            self.literalValue += '*'
        else:
            if self.isLiteralStarted:
                self._tokensList.addLiteralToken( self.literalValue )
                self.isLiteralStarted = False
            self._tokensList.addSimpleToken( STAR )
        return

    def _processPlus(self):
        if self.isStringStarted:
            self.literalValue += '+'
        else:
            if self.isLiteralStarted:
                self._tokensList.addLiteralToken( self.literalValue )
                self.isLiteralStarted = False
        return

    def _processMinus(self):
        if self.isStringStarted:
            self.literalValue += '-'
        else:
            if self.isLiteralStarted:
                self._tokensList.addLiteralToken( self.literalValue )
                self.isLiteralStarted = False
        return

    def _processEqual(self):
        if self.isStringStarted:
            self.literalValue += '='
        else:
            if self.isLiteralStarted:
                self._processFoundLiteral()
                self.isLiteralStarted = False
            self._tokensList.addSimpleToken(ASSIGNMENT)
        return

    def _processFoundDirective(self):
        if self.literalValue in self.knownDirectives:
            self._tokensList.addSimpleToken( self.knownDirectives[self.literalValue] )
            self.isDirectiveStarted = False
        else:
            self._tokensList.addSimpleToken(UNKNOWN)
        return

    def _processFoundLiteral(self):
        if self.literalValue in self._knownKeywords:
            self._tokensList.addSimpleToken( self._knownKeywords[self.literalValue] )
        else:
            self._tokensList.addLiteralToken( self.literalValue )
        self.isLiteralStarted = False
        return

    def _tryToCompletePreviousToken(self, c):
        if not self.isStringStarted:
            if not self.isPunctuatorComplete:
                if self._previousCharacter == '+':
                    if c == '+':
                        self._tokensList.addSimpleToken( INCREMENT )
                    else:
                        self._tokensList.addSimpleToken( ADDITION )
                    self.isPunctuatorComplete = True

                elif self._previousCharacter == '-':
                    if c == '-':
                        self._tokensList.addSimpleToken( DECREMENT )
                    else:
                        self._tokensList.addSimpleToken( SUBTRACTION )
                    self.isPunctuatorComplete = True
            else:
                if c in ['+',',','-']:
                    self.isPunctuatorComplete = False

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
            if self.isLiteralStarted:
                self._processFoundLiteral()
            elif self.isDirectiveStarted:
                self._processFoundDirective()
            self._tokensList.addSimpleToken( EOL )

        return

    def _parseLine(self, inputString):
        self.parseDefine(inputString)
        return


    def parseText(self, text):
        self._clearState()
        for line in text:
            self._parseLine(line)

        if self.isLiteralStarted:
            self._tokensList.addLiteralToken( self.literalValue )

        return self._tokensList.getList()