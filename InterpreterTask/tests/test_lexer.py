import unittest
from Compiler.lexer import Lexer
from Compiler.token import TokenType, Token


class TestLexer(unittest.TestCase):

    def test_get_next_token_sucess(self):
        lexer = Lexer("1 + 5")
        self.assertEqual(lexer.get_next_token(), Token(TokenType.INTEGER, 1))

    def test_reset_sucess(self):
        lexer = Lexer("1+1")
        lexer.pos = 3
        lexer.reset()
        self.assertEqual(lexer.pos, 0)
