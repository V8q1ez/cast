__author__ = 'V8q1ez'

from src.castle.cinderella import cinderella
from src.castle.prince import prince

class enchantress():
    def __init__(self):
        self._cinderella = cinderella()
        self._prince = prince()

    def formatText(self, rawText):
        tokens = self._cinderella.parseText(rawText)
        formattedText = self._prince.buildFormattedText(tokens)
        return formattedText
