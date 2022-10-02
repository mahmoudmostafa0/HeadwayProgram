import enum


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


class Token:
    """
    class that is used to create token
    """

    def __init__(self, token_type: TokenType, value):
        """

        Args:
            token_type: type of the token to be created
            value: value of the token
        """
        self.type = token_type
        self.value = value

    def __eq__(self, other):
        """
        when using == operator with token
        """
        if type(self) == type(other):
            return self.value == other.value and self.type == other.type
        else:
            print("cannot compare variable of type ", type(self), "with another one of type ", type(other))
            raise TypeError

    def __str__(self):
        """String representation of the class instance.
        Examples:
            Token(INTEGER, 3)
            Token(PLUS, '+')
            Token(MUL, '*')
        """
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()
