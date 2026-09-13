from ..ast.expression import ExpressionVisitor, Expression, Literal, Variable, BinaryOperation, UnaryOperation
from ..ast.statement import StatementVisitor, Statement, ExpressionStatement, Assign, ConsoleLog
from .environment import Environment


class Interpreter(ExpressionVisitor, StatementVisitor):
    def __init__(self):
        self.global_env = Environment()
    

    # ===== interpret ===== #
    def interpret(self, statements_list: list[Statement]):
        # interpret program => turn all teo statements into python
        
        for statement in statements_list:
            self.execute(statement)
        
    
    def execute(self, statement: Statement):
        # turn statement into python code
        return statement.accept(self)
    
    
    def evaluate(self, expression: Expression):
        # evaluate expression
        return expression.accept(self)


    # ===== visit expressions ===== #
    def visit_literal(self, literal: "Literal"):
        return literal.value
    
    
    def visit_variable(self, variable: "Variable"):
        return self.global_env.get(variable.name)
    
    
    def visit_binary_operation(self, binary_operation: "BinaryOperation"):
        left = self.evaluate(binary_operation.left)
        operator = binary_operation.operator
        right = self.evaluate(binary_operation.right)
        
        match operator:
            case "+":
                result = left + right
            case "-":
                result = left - right
            case "*":
                result = left * right
            case "/":
                result = left / right
            case _:
                raise SyntaxError(f"Invalid binary operator '{operator}'")
        
        return result
    
    
    def visit_unary_operation(self, unary_operation: "UnaryOperation"):
        operator = unary_operation.operator
        right = self.evaluate(unary_operation.right)
        
        match operator:
            case "-":
                result = -right
            case "+":
                result = right
            case _:
                raise SyntaxError(f"Invalid unary operator '{operator}'")
        
        return result


    # ===== visit statements ===== #
    def visit_expression_statement(self, expression_statement: "ExpressionStatement"):
        return self.evaluate(expression_statement.expression)
    
    
    def visit_assign(self, assign: "Assign"):
        if assign.is_local:
            not_defined = self.global_env.define(assign.name, self.evaluate(assign.value))
            
            if not not_defined:
                raise NameError(f"Local variable '{assign.name}' already defined")
            
            return 0
            
        self.global_env.assign(assign.name, self.evaluate(assign.value))
        
        return 0     
        
    
    def visit_console_log(self, console_log: "ConsoleLog"):
        print(self.evaluate(console_log.output))
        return 0
