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
# BACKSLASH_NEWLINE = 10
STRING = 11
EOL = 12

class directivesDict(dict):
    def __init__(self):
        self['include'] = INCLUDE
        # by default we always interpret definition as an object-like macros
        self['define'] = OBJECT_LIKE_MACRO

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

    def _clearState(self):
        self.isLiteralStarted = False
        self.isStringStarted = False
        self.isEscSeqStarted = False
        self.isTypeOfMacrosKnown = False
        self.literalValue = ''
        self.isDirectiveStarted = False

    """
    All used preprocessor rules are taken from:
        https://gcc.gnu.org/onlinedocs/cpp/index.html
    """

    def parseDefine(self, remainingString):

        for c in remainingString:

            if c == '(':
                self._processLeftParenthesis()

            elif c == ')':
                self._processRightParenthesis()

            elif c == '\\':
                if not self.isEscSeqStarted:
                    self.isEscSeqStarted = True

            elif c == ',':
                self._processComma()

            elif c == '"':
                self._processQuote()

            elif c == '#':
                self._processSharp()

            elif c != ' ':
                self._processNonSpace( c )

            elif c == ' ':
                self._processSpace()

        self._processEndOfLine()

        return

    def _processLeftParenthesis(self):
        if self.isLiteralStarted:
            if not self.isTypeOfMacrosKnown:
                # There is no space between name and parenthesis
                # So we should change the type of first token
                self._tokensList.changeTokenType( 0, FUNCTION_LIKE_MACRO )
                self.isTypeOfMacrosKnown = True
                # and write the macros name
            self._tokensList.addLiteralToken( self.literalValue )
            self.isLiteralStarted = False

        self._tokensList.addSimpleToken( PARENTHESIS_LEFT )

        return

    def _processRightParenthesis(self):
        if self.isLiteralStarted:
            if self.literalValue == '...':
                self._tokensList.addSimpleToken( VARIADIC_ARGS )
            else:
                self._tokensList.addLiteralToken( self.literalValue )
            self.isLiteralStarted = False

        self._tokensList.addSimpleToken( PARENTHESIS_RIGHT )

        return

    def _processComma(self):
        if self.isLiteralStarted:
            if self.literalValue == '...':
                self._tokensList.addSimpleToken( VARIADIC_ARGS )
            else:
                self._tokensList.addLiteralToken( self.literalValue )
            self.isLiteralStarted = False
        self._tokensList.addSimpleToken( COMMA )

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
            if self.literalValue in self.knownDirectives:
                self._tokensList.addSimpleToken( self.knownDirectives[self.literalValue] )
                self.isDirectiveStarted = False
            else:
                self._tokensList.addSimpleToken(UNKNOWN)
        elif self.isStringStarted:
            self.literalValue += ' '
        elif self.isLiteralStarted:
            # since literal finishes by space - this is an object like macros
            self.isTypeOfMacrosKnown = True
            if self.literalValue == '...':
                self._tokensList.addSimpleToken( VARIADIC_ARGS )
            else:
                self._tokensList.addLiteralToken( self.literalValue )
            self.isLiteralStarted = False

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
        if not self.isDirectiveStarted:
            self.literalValue = ''
            self.isDirectiveStarted = True
        return

    def _processEndOfLine(self):
        if self.isEscSeqStarted:
            if self.isLiteralStarted:
                self._tokensList.addLiteralToken( self.literalValue )
                self.isLiteralStarted = False
            # esc sequence cannot be between two lines
            self.isEscSeqStarted = False
        else:
            if self.isLiteralStarted:
                self._tokensList.addLiteralToken( self.literalValue )
                self.isLiteralStarted = False
            self._tokensList.addSimpleToken( EOL )

        return

    def _parseLine(self, inputString):
        self.parseDefine(inputString)
        return


    def parseText(self, text):
        self._clearState()
        for line in text:
            self._parseLine(line)

        return self._tokensList.getList()