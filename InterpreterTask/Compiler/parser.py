from Compiler.lexer import TokenType
from Compiler.Tree.BinaryOperators.divide_operator import DivOP
from Compiler.Tree.BinaryOperators.minus_operator import MinusOP
from Compiler.Tree.BinaryOperators.multiply_operator import MulOP
from Compiler.Tree.BinaryOperators.plus_operator import PlusOP
from Compiler.Tree.function_call_node import FuncCallNode
from Compiler.Tree.num_node import Num
from Compiler.Tree.string_node import String
from Compiler.Tree.UnaryOperators.negative_unary import NegativeUnary
from Compiler.Tree.UnaryOperators.positive_unary import PositiveUnary
from Compiler.Tree.variable_node import Var


class Parser:
    """
    Class for parsing KPI expression into abstract syntax tree
    """

    def __init__(self, lexer):
        self.lexer = lexer
        # set current token to the first token taken from the input
        self.current_token = self.lexer.get_next_token()

    def reset(self):
        """
        function that is used to reset the parser class
        """
        self.lexer.reset()
        self.current_token = self.lexer.get_next_token()

    def error(self):
        """
        thorws an error
        """
        raise Exception('Invalid syntax')

    def eat(self, token_type):
        """
        compare the current token type with the passed token
        type and if they match then "eat" the current token
        and assign the next token to the self.current_token,
        otherwise raise an exception.
        Args:
            token_type: type of the token to eat

        """
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self):
        """factor : (PLUS | MINUS) factor | INTEGER | LPAREN expr RPAREN | string | variable"""
        token = self.current_token
        if token.type == TokenType.PLUS:
            self.eat(TokenType.PLUS)
            return PositiveUnary(self.factor())
        if token.type == TokenType.MINUS:
            self.eat(TokenType.MINUS)
            return NegativeUnary(self.factor())
        if token.type == TokenType.INTEGER:
            self.eat(TokenType.INTEGER)
            return Num(token)
        if token.type == TokenType.LPAREN:
            self.eat(TokenType.LPAREN)
            node = self.expr()
            self.eat(TokenType.RPAREN)
            return node
        if token.type == TokenType.STRING:
            self.eat(TokenType.STRING)
            return String(token)
        if token.type == TokenType.IDENTIFIER:
            return self.variable()
        self.error()

    def term(self):
        """term : factor ((MUL | DIV) factor)*"""
        node = self.factor()

        while self.current_token.type in (TokenType.MUL, TokenType.DIV):
            token = self.current_token
            if token.type == TokenType.MUL:
                self.eat(TokenType.MUL)
                node = MulOP(node, token, self.factor())
            elif token.type == TokenType.DIV:
                self.eat(TokenType.DIV)
                node = DivOP(node, token, self.factor())

        return node

    def variable(self):
        """
        variable : ID
        """
        node = Var(self.current_token)
        self.eat(TokenType.IDENTIFIER)
        return node

    def functioncall(self):
        """functioncall : ID LPAREN (expr (COMMA expr)*)? RPAREN"""

        proc_name = self.current_token.value
        self.eat(TokenType.IDENTIFIER)
        self.eat(TokenType.LPAREN)
        params = []
        if self.current_token.type != TokenType.RPAREN:
            params.append(self.expr())

        while self.current_token.type == TokenType.COMMA:
            self.eat(TokenType.COMMA)
            params.append(self.expr())

        self.eat(TokenType.RPAREN)

        node = FuncCallNode(proc_name, params)
        return node

    def expr(self):
        """expr   : term ((PLUS | MINUS) term)* """
        node = self.term()

        while self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            token = self.current_token
            if token.type == TokenType.PLUS:
                self.eat(TokenType.PLUS)
                node = PlusOP(node, token, self.term())
            if token.type == TokenType.MINUS:
                self.eat(TokenType.MINUS)
                node = MinusOP(node, token, self.term())

        return node

    def program(self):
        """
        program : functioncall|expr
        functioncall : IDENTIFIER LPAREN (expr (COMMA expr)*)? RPAREN
        expr   : term ((PLUS | MINUS) term)*
        term   : factor ((MUL | DIV) factor)*
        factor : (PLUS | MINUS) factor | INTEGER | LPAREN expr RPAREN | variable | string
        """

        next_token = self.lexer.peek_next_token()
        if self.current_token.type == TokenType.IDENTIFIER and next_token.type == TokenType.LPAREN:
            return self.functioncall()

        return self.expr()

    def parse(self):
        """
        parse all construct tree
        """
        node = self.program()
        if self.current_token.type != TokenType.EOF:
            self.error()
        return node
