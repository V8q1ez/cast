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

    def changeTokenType(self, index, newType):
        self.tokensList[ index ].type = newType

    def getList(self):
        return self.tokensList


class tokenizer():
    def __init__(self):
        self.tokensList = tokenList()

    """
    The argument of ‘#include’, whether delimited with quote marks or angle brackets,
        behaves like a string constant in that comments are not recognized,
        and macro names are not expanded. Thus,
        #include <x/*y> specifies inclusion of a system header file named x/*y.

    However, if backslashes occur within file, they are considered ordinary text characters,
        not escape characters. None of the character escape sequences appropriate to string
        constants in C are processed. Thus, #include "x\n\\y" specifies a filename containing
        three backslashes. (Some systems interpret ‘\’ as a pathname separator.
        All of these also interpret ‘/’ the same way. It is most portable to use only ‘/’.)

    It is an error if there is anything (other than comments) on the line after the file name.

    source:  https://gcc.gnu.org/onlinedocs/cpp/Include-Syntax.html#Include-Syntax
    """
    def parseInclude(self, remainingString):
        self.tokensList.addSimpleToken( INCLUDE )
        # try to find first '"' or '<'
        self.isLiteralStarted = False
        literalValue = ''
        for c in remainingString:
            if c == '"':
                if self.isLiteralStarted == False:
                    self.tokensList.addSimpleToken( QUOTE )
                    self.isLiteralStarted = True
                else:
                    self.tokensList.addLiteralToken( literalValue )
                    self.tokensList.addSimpleToken( QUOTE )
                    self.isLiteralStarted = False
            elif self.isLiteralStarted == True:
                literalValue += c

        return

    def parseDefine(self, remainingString):
        self.tokensList.addSimpleToken( OBJECT_LIKE_MACRO )

        self.isLiteralStarted = False
        literalValue = ''
        isTypeOfMacrosKnown = False
        for c in remainingString:

            if c == '(':
                if self.isLiteralStarted == True:
                    if isTypeOfMacrosKnown == False:
                        # There is no space between name and parenthesis
                        # So we should change the type of first token
                        self.tokensList.changeTokenType( 0, FUNCTION_LIKE_MACRO )
                        isTypeOfMacrosKnown = True
                        # and write the macros name
                    self.tokensList.addLiteralToken( literalValue )
                    self.isLiteralStarted = False

                self.tokensList.addSimpleToken( PARENTHESIS_LEFT )

            elif c == ')':
                if self.isLiteralStarted == True:
                    if literalValue == '...':
                        self.tokensList.addSimpleToken( VARIADIC_ARGS )
                    else:
                        self.tokensList.addLiteralToken( literalValue )
                    self.isLiteralStarted = False

                self.tokensList.addSimpleToken( PARENTHESIS_RIGHT )

            elif c == ',':
                if self.isLiteralStarted == True:
                    if literalValue == '...':
                        self.tokensList.addSimpleToken( VARIADIC_ARGS )
                    else:
                        self.tokensList.addLiteralToken( literalValue )
                    self.isLiteralStarted = False
                self.tokensList.addSimpleToken( COMMA )

            elif c != ' ':
                if self.isLiteralStarted == False:
                    literalValue = c
                    self.isLiteralStarted = True
                else:
                    literalValue += c

            elif c == ' ':
                if self.isLiteralStarted == True:
                    # since literal finishes by space - this is an object like macros
                    isTypeOfMacrosKnown = True
                    if literalValue == '...':
                        self.tokensList.addSimpleToken( VARIADIC_ARGS )
                    else:
                        self.tokensList.addLiteralToken( literalValue )
                    self.isLiteralStarted = False

        # if end of line but literal was started
        if self.isLiteralStarted == True:
            self.tokensList.addLiteralToken( literalValue )

        return

    def getFirstToken(self, inputString):
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


    def parseString(self, inputString):
        parts = inputString.split()
        inputString = ' '.join(parts)

        (firstToken, nextPos) = self.getFirstToken(inputString)

        if firstToken.type == INCLUDE:
            self.parseInclude(inputString[nextPos:])

        elif firstToken.type == OBJECT_LIKE_MACRO:
            self.parseDefine(inputString[nextPos:])

        return self.tokensList.getList()
