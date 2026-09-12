from teo.lexer.lexer import Token
from teo.ast.expression import Literal, Variable, BinaryOperation, UnaryOperation
from teo.ast.statement import ExpressionStatement, Assignment, ConsoleLog, Statement


class Parser:
    def __init__(self, tokens: list[Token]):
        self.tokens = tokens
        self.current = 0
        
        
    def parse(self) -> list[Statement]:
        pass

    
    def parse_statement(self) -> list[Statement]:
        pass

    
    def parse_expression(self) -> list[Statement]:
        pass
    
    
    def parse_addition(self) -> list[Statement]:
        pass
    
    
    def parse_multiplication(self) -> list[Statement]:
        pass
    
    
    def parse_unary(self) -> list[Statement]:
        pass
    
    
    def parse_primary(self) -> list[Statement]:
        pass
        