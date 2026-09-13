from ..ast.expression import Expression, Literal, Variable, BinaryOperation, UnaryOperation
from ..ast.statement import Statement, ExpressionStatement, Assign, ConsoleLog
from .environment import Environment


class Interpreter:
    def __init__(self):
        self.global_env = Environment()
    

    def interpret(self, statements_list: list[Statement]):
        # interpret program => turn all teo statements into python
        ...
        
    
    def execute(self, statement: Statement):
        # turn statement into python code
        ...
    
    
    def evaluate(self, expression: Expression):
        # evaluate expression
        ...