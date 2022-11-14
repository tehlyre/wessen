from enum import Enum

class Tokentype(Enum):
    PLUS = 0x0001
    MINUS = 0x0002
    MULT = 0x0003
    DIV = 0x0004
    LPAR = 0x0005
    RPAR = 0x0006
    # datatypes
    INT = 0x1000

class Lexer:

    def __init__(self, text):
        self.text = text
        self.pos = -1
        print(self.nextChar())
        self.lexicalAnalysis()

    def lexicalAnalysis(self):
            while self.text[self.pos] is not None:
                try:
                    print(self.nextChar())
                except IndexError:
                    pass


    def nextChar(self):
        self.pos += 1
        return self.text[self.pos] if self.pos < len(self.text) else None

    def peek(self):
        pass
