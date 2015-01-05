__author__ = 'V8q1ez'

from collections import deque
from src.castle.incantations import *


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

    def addSingleLineCommentToken(self, literalValue):
        t = token(SINGLE_LINE_COMMENT)
        t.literalValue = literalValue
        self.tokensList.append(t)

    def addMultiLineCommentLineToken(self, literalValue):
        t = token(MULTI_LINE_COMMENT_LINE)
        t.literalValue = literalValue
        self.tokensList.append(t)

    def changeTokenType(self, index, newType):
        self.tokensList[ index ].type = newType

    def getList(self):
        return self.tokensList


class cinderella():
    def __init__(self):
        self._tokensList = tokenList()
        self.knownDirectives = directivesDict()
        self._knownKeywords = keyWordsDict()
        self._singlePunctuators = singlePunctuatorDict()
        self._pairPunctuatorsDict = pairPunctuatorDict()
        self._triplePunctuatorsDict = triplePunctuatorDict()
        self._punctuatorsCache = deque()

        self._characterHandlersDict = {
            '(' : self._processLeftParenthesis,
            ')' : self._processRightParenthesis,
            '{' : self._processLeftBrace,
            '}' : self._processRightBrace,
            ',' : self._processComma,
            ';' : self._processSemicolon,
            ':' : self._processColon,
            '"' : self._processQuote,
            '#' : self._processHash,
            '%' : self._processPercent,
            '*' : self._processAsterisk,
            '&' : self._processAmpersand,
            '/' : self._processSlash,
            '+' : self._processPlus,
            '-' : self._processMinus,
            '=' : self._processEqual,
            '[' : self._processSquareBracketLeft,
            ']' : self._processSquareBracketRight,
            ' ' : self._processSpace,
            '!' : self._processExclamationMark,
            '<' : self._processLeftAngleBracket,
            '>' : self._processRightAngleBracket,
            '|' : self._processVerticalBar,
            '~' : self._processTilde,
            '^' : self._processCaret,
            '?' : self._processQuestionMark,
            }

    def _clearState(self):
        self.isLiteralStarted = False
        self.isStringStarted = False
        self.isEscSeqStarted = False
        self.isTypeOfMacrosKnown = True
        self.literalValue = ''
        self.isDirectiveStarted = False
        self.isSingleLineCommentStarted = False
        self.isMultiLineCommentStarted = False

    """
    All used preprocessor rules are taken from:
        https://gcc.gnu.org/onlinedocs/cpp/index.html
    """

    def parseLine(self, remainingString):


        for c in remainingString:

            if self.isSingleLineCommentStarted:
                self.literalValue += c
                continue

            self._tryToCompletePreviousToken( c )

            if c in self._characterHandlersDict:
                handlerToCall = self._characterHandlersDict[ c ]
                handlerToCall()

            elif c == '\\':
                if not self.isEscSeqStarted:
                    self.isEscSeqStarted = True

            elif c != ' ':
                self._processNonSpace( c )

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

    def _processLeftAngleBracket(self):
        if self.isStringStarted:
            self.literalValue += '<'
        else:
            if self.isLiteralStarted:
                self._processFoundLiteral()
        return

    def _processRightAngleBracket(self):
        if self.isStringStarted:
            self.literalValue += '>'
        else:
            if self.isLiteralStarted:
                self._processFoundLiteral()
        return

    def _processVerticalBar(self):
        if self.isStringStarted:
            self.literalValue += '|'
        else:
            if self.isLiteralStarted:
                self._processFoundLiteral()
        return

    def _processTilde(self):
        if self.isStringStarted:
            self.literalValue += '~'
        else:
            if self.isLiteralStarted:
                self._processFoundLiteral()
        return

    def _processCaret(self):
        if self.isStringStarted:
            self.literalValue += '^'
        else:
            if self.isLiteralStarted:
                self._processFoundLiteral()
        return

    def _processQuestionMark(self):
        if self.isStringStarted:
            self.literalValue += '?'
        else:
            if self.isLiteralStarted:
                self._processFoundLiteral()
        return

    def _processExclamationMark(self):
        if self.isStringStarted:
            self.literalValue +='!'
        else:
            if self.isLiteralStarted:
                self._processFoundLiteral()
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
        elif self.isStringStarted or self.isSingleLineCommentStarted:
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

    def _processHash(self):
        if self.isStringStarted:
            self.literalValue += '#'
        else:
            if not self.isDirectiveStarted:
                self.literalValue = ''
                self.isDirectiveStarted = True
                self.isTypeOfMacrosKnown = False
        return

    def _processPercent(self):
        if self.isStringStarted:
            self.literalValue += '%'
        else:
            if self.isLiteralStarted:
                self._processFoundLiteral()
        return

    def _processAsterisk(self):
        if self.isStringStarted:
            self.literalValue += '*'
        else:
            if self.isLiteralStarted:
                self._processFoundLiteral()
        return

    def _processAmpersand(self):
        if self.isStringStarted:
            self.literalValue += '&'
        else:
            if self.isLiteralStarted:
                self._tokensList.addLiteralToken( self.literalValue )
                self.isLiteralStarted = False
        return

    def _processSlash(self):
        if self.isStringStarted:
            self.literalValue += '/'
        else:
            if self.isLiteralStarted:
                self._processFoundLiteral()
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
        return

    def _processFoundDirective(self):
        if self.literalValue in self.knownDirectives:
            self._tokensList.addSimpleToken( self.knownDirectives[self.literalValue] )
            self.isDirectiveStarted = False
            if self.literalValue != 'define':
                self.isTypeOfMacrosKnown = True
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
            if c in self._singlePunctuators:
                self._punctuatorsCache.append(c)
            else:
                self._processCachedPunctuators()

        return

    def _processCachedPunctuators(self):
        punctuator = UNKNOWN
        while len(self._punctuatorsCache):

            if len(self._punctuatorsCache) >= 3:
                lastThreeChars = ''.join(list(self._punctuatorsCache)[0:3])
                firstTwoChars = ''.join(list(self._punctuatorsCache)[0:2])
                char = ''.join(list(self._punctuatorsCache)[0:1])
                if lastThreeChars in self._triplePunctuatorsDict:
                    punctuator = self._triplePunctuatorsDict[ lastThreeChars ]
                    for _ in range(3):
                        self._punctuatorsCache.popleft()
                elif firstTwoChars in self._pairPunctuatorsDict:
                    punctuator = self._pairPunctuatorsDict[ firstTwoChars ]
                    for _ in range(2):
                        self._punctuatorsCache.popleft()
                elif char in self._singlePunctuators:
                    punctuator = self._singlePunctuators[ char ]
                    for _ in range(1):
                        self._punctuatorsCache.popleft()

            elif len(self._punctuatorsCache) == 2:
                firstTwoChars = ''.join(list(self._punctuatorsCache)[0:2])
                if firstTwoChars in self._pairPunctuatorsDict:
                    punctuator = self._pairPunctuatorsDict[ firstTwoChars ]
                    for _ in range(2):
                        self._punctuatorsCache.popleft()

            elif len(self._punctuatorsCache) == 1:
                char = ''.join(list(self._punctuatorsCache)[0:1])
                if char in self._singlePunctuators:
                    punctuator = self._singlePunctuators[ char ]
                    for _ in range(1):
                        self._punctuatorsCache.popleft()

            if punctuator != UNKNOWN:
                if punctuator == SINGLE_LINE_COMMENT:
                    self.isSingleLineCommentStarted = True
                    self.literalValue = ''
                elif punctuator == MULTI_LINE_COMMENT_START:
                    self.isMultiLineCommentStarted = True
                    self.literalValue = ''
                elif punctuator == MULTI_LINE_COMMENT_END:
                    self.isMultiLineCommentStarted = False
                    self._tokensList.addMultiLineCommentLineToken( self.literalValue )

                self._tokensList.addSimpleToken( punctuator )
                punctuator = UNKNOWN

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
              self._tokensList.addSingleLineCommentToken( self.literalValue )

            elif self.isLiteralStarted:
                self._processFoundLiteral()
            elif self.isDirectiveStarted:
                self._processFoundDirective()
            else:
                self._processCachedPunctuators()
            self._tokensList.addSimpleToken( EOL )

        return

    def _parseLine(self, inputString):
        self.parseLine(inputString)
        return


    def parseText(self, text):
        self._clearState()
        for line in text:
            self._parseLine(line)

        if self.isLiteralStarted:
            self._tokensList.addLiteralToken( self.literalValue )

        return self._tokensList.getList()