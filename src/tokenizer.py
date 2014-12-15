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
        self.tokensList = tokenList()

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

            elif c != ' ':
                self._processNonSpace( c )

            elif c == ' ':
                self._processSpace()

        # if end of line
        if self.isEscSeqStarted == True:
            if self.isLiteralStarted == True:
                self.tokensList.addLiteralToken( self.literalValue )
                self.isLiteralStarted = False
            self.tokensList.addSimpleToken( BACKSLASH_NEWLINE )
        else:
            if self.isLiteralStarted == True:
                self.tokensList.addLiteralToken( self.literalValue )
                self.isLiteralStarted = False

        self.tokensList.addSimpleToken( EOL )

        return

    def _processLeftParenthesis(self):
        if self.isLiteralStarted == True:
            if self.isTypeOfMacrosKnown == False:
                # There is no space between name and parenthesis
                # So we should change the type of first token
                self.tokensList.changeTokenType( 0, FUNCTION_LIKE_MACRO )
                isTypeOfMacrosKnown = True
                # and write the macros name
            self.tokensList.addLiteralToken( self.literalValue )
            self.isLiteralStarted = False

        self.tokensList.addSimpleToken( PARENTHESIS_LEFT )

        return

    def _processRightParenthesis(self):
        if self.isLiteralStarted == True:
            if self.literalValue == '...':
                self.tokensList.addSimpleToken( VARIADIC_ARGS )
            else:
                self.tokensList.addLiteralToken( self.literalValue )
            self.isLiteralStarted = False

        self.tokensList.addSimpleToken( PARENTHESIS_RIGHT )

        return

    def _processComma(self):
        if self.isLiteralStarted == True:
            if self.literalValue == '...':
                self.tokensList.addSimpleToken( VARIADIC_ARGS )
            else:
                self.tokensList.addLiteralToken( self.literalValue )
            self.isLiteralStarted = False
        self.tokensList.addSimpleToken( COMMA )

        return

    def _processQuote(self):
        if self.isStringStarted == True:
            if self.isEscSeqStarted == True:
                self.literalValue += '\\\"'
                self.isEscSeqStarted = False
            else:
                self.tokensList.addStringToken( self.literalValue )
                self.isStringStarted = False
                self.tokensList.addSimpleToken( QUOTE )
        else:
            if self.isLiteralStarted == True:
                self.tokensList.addLiteralToken( self.literalValue )
                self.isLiteralStarted = False
            else:
                self.literalValue = ''
                self.isStringStarted = True
            self.tokensList.addSimpleToken( QUOTE )

        return

    def _processSpace(self):
        if self.isStringStarted == True:
            self.literalValue += ' '
        elif self.isLiteralStarted == True:
            # since literal finishes by space - this is an object like macros
            self.isTypeOfMacrosKnown = True
            if self.literalValue == '...':
                self.tokensList.addSimpleToken( VARIADIC_ARGS )
            else:
                self.tokensList.addLiteralToken( self.literalValue )
            self.isLiteralStarted = False

        return

    def _processNonSpace(self, c):
        if self.isStringStarted == True:
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

    def _getFirstToken(self, inputString):
        curPos = 0
        firstToken = ''
        isItPreprocessorDirective = False
        result = token(UNKNOWN)
        for c in inputString:
            if c == '#' and curPos == 0:
                isItPreprocessorDirective = True
            elif c == '_' or c.isalnum():
                firstToken += c
            else:
                if isItPreprocessorDirective:
                    if firstToken == 'include':
                        result.type = INCLUDE
                    elif firstToken == 'define':
                        result.type = OBJECT_LIKE_MACRO

            curPos += 1
            if result.type != UNKNOWN:
                return (result, curPos)

        return (result, 0)


    def parseLine(self, inputString):
        #parts = inputString.split()
        #inputString = ' '.join(parts)

        (firstToken, nextPos) = self._getFirstToken(inputString)

        if firstToken.type == INCLUDE:
            self.tokensList.addSimpleToken( INCLUDE )
            self.parseDefine(inputString[nextPos:])

        elif firstToken.type == OBJECT_LIKE_MACRO:
            self.tokensList.addSimpleToken( OBJECT_LIKE_MACRO )
            self.parseDefine(inputString[nextPos:])

        return self.tokensList.getList()
