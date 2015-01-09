__author__ = 'V8q1ez'

from collections import deque
from src.castle.incantations import *


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
            '"' : self._processQuote,
            ' ' : self._processSpace,
            }

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

    """
    All used preprocessor rules are taken from:
        https://gcc.gnu.org/onlinedocs/cpp/index.html
    """

    def parseLine(self, remainingString):


        for c in remainingString:

            if self.isSingleLineCommentStarted:
                self.literalValue += c
                continue

            elif c == '\\':
                if not self.isEscSeqStarted:
                    self.isEscSeqStarted = True
                    continue

            self._tryToCompletePreviousToken( c )

            if c in self._singlePunctuators:
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
          self._tokensList.addSimpleToken( FUNCTION_LIKE_MACRO )
          self._tokensList.addLiteralToken( self.literalValue )
          self.isNameOfMacrosNeeded = False
          self._tokensList.addSimpleToken( PARENTHESIS_LEFT )

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
            self._tokensList.addSimpleToken( PARENTHESIS_LEFT )

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
                self._processFoundLiteral()
            else:
                self.literalValue = ''
                self.isStringStarted = True
            self._tokensList.addSimpleToken( QUOTE )

        return

    def _processSpace(self):
        if self.isDirectiveStarted:
            self._processFoundDirective()
        elif self.isNameOfMacrosNeeded:
            self._lastFoundMacrosName = self.literalValue
            self.isNameOfMacrosNeeded = False
            self._tokensList.addSimpleToken(OBJECT_LIKE_MACRO)
            self._tokensList.addLiteralToken( self.literalValue )
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
        if self.literalValue in self.knownDirectives:
            self.isDirectiveStarted = False
            if self.literalValue == 'define':
                self.isNameOfMacrosNeeded = True
            else:
                self._tokensList.addSimpleToken( self.knownDirectives[self.literalValue] )
        else:
            self._tokensList.addSimpleToken(UNKNOWN)
        self.literalValue = ''
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

            if self.isSingleLineCommentStarted:
                self.literalValue += self._punctuatorsCache.popleft()

            elif self.isMultiLineCommentStarted:
                # only MULTI_LINE_COMMENT_END of EOL are allowed
                if len(self._punctuatorsCache) >= 2:
                    firstTwoChars = ''.join(list(self._punctuatorsCache)[0:2])
                    if firstTwoChars in self._pairPunctuatorsDict:
                        punctuator = self._pairPunctuatorsDict[ firstTwoChars ]
                    if punctuator == MULTI_LINE_COMMENT_END:
                        for _ in range(2):
                            self._punctuatorsCache.popleft()
                        self.isMultiLineCommentStarted = False
                        self._tokensList.addMultiLineCommentLineToken( self.literalValue )
                        self._tokensList.addSimpleToken( punctuator )
                    else:
                        self.literalValue += self._punctuatorsCache.popleft()
                else:
                    self.literalValue += self._punctuatorsCache.popleft()
            else:
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
                    char = ''.join(list(self._punctuatorsCache)[0:1])
                    if firstTwoChars in self._pairPunctuatorsDict:
                        punctuator = self._pairPunctuatorsDict[ firstTwoChars ]
                        for _ in range(2):
                            self._punctuatorsCache.popleft()
                    elif char in self._singlePunctuators:
                        punctuator = self._singlePunctuators[ char ]
                        for _ in range(1):
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
                    elif punctuator == HASH:
                        if not self.isStringStarted and not self.isDirectiveStarted:
                            self.literalValue = ''
                            self.isDirectiveStarted = True
                            self.isNameOfMacrosNeeded = False
                    else:
                        if punctuator == MULTI_LINE_COMMENT_START:
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
                self.isSingleLineCommentStarted = False

            elif self.isLiteralStarted:
                self._processFoundLiteral()
            elif self.isDirectiveStarted:
                self._processFoundDirective()
            elif self.isNameOfMacrosNeeded:
                self._lastFoundMacrosName = self.literalValue
                self.isNameOfMacrosNeeded = False
                self._tokensList.addSimpleToken(OBJECT_LIKE_MACRO)
                self._tokensList.addLiteralToken( self.literalValue )
            else:
                self._processCachedPunctuators()
                if self.isMultiLineCommentStarted:
                    self._tokensList.addMultiLineCommentLineToken(self.literalValue)
                    self.literalValue = ''
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