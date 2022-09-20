# Token types
#
# EOF (end-of-file) token is used to indicate that
# there is no more input left for lexical analysis
import enum

from Compiler.token import Token


class TokenType(enum.Enum):
    """
    enum for the token type
    """
    EOF = -1
    INTEGER = 1
    PLUS = '+'
    MINUS = '-'
    MUL = '*'
    DIV = '/'
    LPAREN = '('
    RPAREN = ')'
    COMMA = ','
    IDENTIFIER = 9
    IF = 10
    STRING = 11


class Lexer:
    """
    lexer class for the interpreter
    """
    def __init__(self, text):
        # client string input, e.g. "4 + 2 * 3 - 6 / 2"
        self.text = text
        # self.pos is an index into self.text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def reset(self):
        """
        reset the lexer class
        """
        self.__init__(self.text)

    def error(self):
        """
        raise an error
        """
        raise Exception('Invalid character')

    def advance(self):
        """Advance the `pos` pointer and set the `current_char` variable."""
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None  # Indicates end of input
        else:
            self.current_char = self.text[self.pos]

    def peek_next_token(self) -> Token:
        """returns the next token without manuplating the current index of the char"""
        currentpos = self.pos - 1
        nexttoken = self.get_next_token()
        self.pos = currentpos
        self.advance()
        return nexttoken

    def skip_whitespace(self):
        """
        keep advacing until there is no whitespaces
        """
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        """Return a (multidigit) integer consumed from the input."""
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def identifier(self):
        """
        returns an identifier
        """
        result = ''
        while self.current_char is not None and self.current_char.isalnum():
            result += self.current_char
            self.advance()

        return Token(TokenType.IDENTIFIER, result)

    def string(self):
        """
        returns a string
        """
        result = ''
        self.advance()
        while self.current_char is not None and self.current_char != '"':
            result += self.current_char
            self.advance()
        self.advance()
        return Token(TokenType.STRING, result)

    def get_next_token(self):
        """Lexical analyzer (also known as scanner or tokenizer)
        This method is responsible for breaking a sentence
        apart into tokens. One token at a time.
        """
        while self.current_char is not None:

            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return Token(TokenType.INTEGER, self.integer())

            if self.current_char.isalpha():
                return self.identifier()
            if self.current_char == '"':
                return self.string()

            knowntokens = [t.value for t in TokenType]
            if self.current_char in knowntokens:
                result = Token(TokenType(self.current_char), self.current_char)
                self.advance()
                return result

            self.error()

        return Token(TokenType.EOF, None)
