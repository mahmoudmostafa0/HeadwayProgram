import unittest
from unittest.mock import Mock

from Compiler.Tree.num_node import Num
from Compiler.lexer import Lexer
from Compiler.parser import Parser
from Compiler.token import TokenType, Token


class TestParser(unittest.TestCase):

    def setUp(self) -> None:
        lexer = Mock()
        lexer.get_next_token.return_value = Token(TokenType.INTEGER, 10)
        self.parser = Parser(lexer)
        pass

    # self.current_token = Token(TokenType.STRING,"aaaa")
    def test_incorrect_eat(self):
        with self.assertRaises(Exception):
            self.parser.eat(TokenType.IDENTIFIER)

    def test_correct_eat(self):
        self.parser.eat(TokenType.INTEGER)

    # @patch('Compiler.parser.Parser.eat')
    def test_correct_variable(self):
        lexer = Lexer("1 + 1 - 2")
        parser = Parser(lexer)
        self.assertEqual(parser.factor().token, Token(TokenType.INTEGER, 1))
        self.assertEqual(parser.factor().token, Token(TokenType.PLUS, Num(Token(TokenType.INTEGER, 1))))
        self.assertEqual(parser.factor().token, Token(TokenType.PLUS, Num(Token(TokenType.INTEGER, 2))))

    def test_incorrect_factor(self):
        lexer = Mock()
        lexer.get_next_token.return_value = Token(TokenType.COMMA, ',')
        parser = Parser(lexer)
        with self.assertRaises(Exception):
            parser.factor()

    def test_variable_correct(self):
        lexer = Mock()
        lexer.get_next_token.return_value = Token(TokenType.IDENTIFIER, 'testtt')
        parser = Parser(lexer)
        self.assertEqual(parser.variable().token, Token(TokenType.IDENTIFIER, 'testtt'))
