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
BACKSLASH_NEWLINE = 10
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

    def getLastToken(self):
        return self.tokensList[-1]

    def getList(self):
        return self.tokensList


class tokenizer():
    def __init__(self):
        self._tokensList = tokenList()
        self.knownDirectives = directivesDict()

    """
    All used preprocessor rules are taken from:
        https://gcc.gnu.org/onlinedocs/cpp/index.html
    """

    def parseDefine(self, remainingString):

        self.isLiteralStarted = False
        self.isStringStarted = False
        self.isEscSeqStarted = False
        self.isTypeOfMacrosKnown = False
        self.literalValue = ''
        self.isDirectiveStarted = False

        for c in remainingString:

            if c == '(':
                self._processLeftParenthesis()

            elif c == ')':
                self._processRightParenthesis()

            elif c == '\\':
                if self.isEscSeqStarted == False:
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
        if self.isLiteralStarted == True:
            if self.isTypeOfMacrosKnown == False:
                # There is no space between name and parenthesis
                # So we should change the type of first token
                self._tokensList.changeTokenType( 0, FUNCTION_LIKE_MACRO )
                isTypeOfMacrosKnown = True
                # and write the macros name
            self._tokensList.addLiteralToken( self.literalValue )
            self.isLiteralStarted = False

        self._tokensList.addSimpleToken( PARENTHESIS_LEFT )

        return

    def _processRightParenthesis(self):
        if self.isLiteralStarted == True:
            if self.literalValue == '...':
                self._tokensList.addSimpleToken( VARIADIC_ARGS )
            else:
                self._tokensList.addLiteralToken( self.literalValue )
            self.isLiteralStarted = False

        self._tokensList.addSimpleToken( PARENTHESIS_RIGHT )

        return

    def _processComma(self):
        if self.isLiteralStarted == True:
            if self.literalValue == '...':
                self._tokensList.addSimpleToken( VARIADIC_ARGS )
            else:
                self._tokensList.addLiteralToken( self.literalValue )
            self.isLiteralStarted = False
        self._tokensList.addSimpleToken( COMMA )

        return

    def _processQuote(self):
        if self.isStringStarted == True:
            if self.isEscSeqStarted == True:
                self.literalValue += '\\\"'
                self.isEscSeqStarted = False
            else:
                self._tokensList.addStringToken( self.literalValue )
                self.isStringStarted = False
                self._tokensList.addSimpleToken( QUOTE )
        else:
            if self.isLiteralStarted == True:
                self._tokensList.addLiteralToken( self.literalValue )
                self.isLiteralStarted = False
            else:
                self.literalValue = ''
                self.isStringStarted = True
            self._tokensList.addSimpleToken( QUOTE )

        return

    def _processSpace(self):
        if self.isDirectiveStarted == True:
            if self.literalValue in self.knownDirectives:
                self._tokensList.addSimpleToken( self.knownDirectives[self.literalValue] )
                self.isDirectiveStarted = False
            else:
                self._tokensList.addSimpleToken(UNKNOWN)
        elif self.isStringStarted == True:
            self.literalValue += ' '
        elif self.isLiteralStarted == True:
            # since literal finishes by space - this is an object like macros
            self.isTypeOfMacrosKnown = True
            if self.literalValue == '...':
                self._tokensList.addSimpleToken( VARIADIC_ARGS )
            else:
                self._tokensList.addLiteralToken( self.literalValue )
            self.isLiteralStarted = False

        return

    def _processNonSpace(self, c):
        if self.isDirectiveStarted == True:
            self.literalValue += c
        elif self.isStringStarted == True:
            if self.isEscSeqStarted == True:
                self.literalValue += '\\'
                self.isEscSeqStarted = False
            self.literalValue += c
        else:
            if self.isLiteralStarted == False:
                self.literalValue = c
                self.isLiteralStarted = True
            else:
                self.literalValue += c
        return

    def _processSharp(self):
        if self.isDirectiveStarted == False:
            self.literalValue = ''
            self.isDirectiveStarted = True
        return

    def _processEndOfLine(self):
        if self.isEscSeqStarted == True:
            if self.isLiteralStarted == True:
                self._tokensList.addLiteralToken( self.literalValue )
                self.isLiteralStarted = False
            self._tokensList.addSimpleToken( BACKSLASH_NEWLINE )
        else:
            if self.isLiteralStarted == True:
                self._tokensList.addLiteralToken( self.literalValue )
                self.isLiteralStarted = False

        if self._tokensList.getLastToken().type != BACKSLASH_NEWLINE:
            self._tokensList.addSimpleToken( EOL )

        return

    def _parseLine(self, inputString):
        self.parseDefine(inputString)
        return


    def parseText(self, text):
        for line in text:
            self._parseLine(line)

        return self._tokensList.getList()