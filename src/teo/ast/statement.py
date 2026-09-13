from .expression import Expression


# visitor class
class StatementVisitor:
    def visit_expression_statement(self, expression_statement: "ExpressionStatement"):
        ...
    
    def visit_assign(self, assign: "Assign"):
        ...
    
    def visit_console_log(self, console_log: "ConsoleLog"):
        ...


# base class
class Statement:
    def accept(self, visitor: StatementVisitor):
        pass


# expression
class ExpressionStatement(Statement):
    def __init__(self, expression: Expression) -> None:
        self.expression = expression
    
    def __repr__(self) -> str:
        return f"ExpressionStatement (expression: {self.expression})"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, ExpressionStatement):
            return NotImplemented
        
        return self.expression == other.expression
    
    def accept(self, visitor: StatementVisitor):
        return visitor.visit_expression_statement(self)


# assign value to variable
class Assign(Statement):
    def __init__(self, name: str, value: Expression, is_local: bool = False) -> None:
        self.name = name
        self.value = value
        self.is_local = is_local
    
    def __repr__(self) -> str:
        return f"Assignment ({self.name} = {self.value})"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Assign):
            return NotImplemented
        
        return (
            self.name == other.name and
            self.value == other.value
        )
    
    def accept(self, visitor: StatementVisitor):
        return visitor.visit_assign(self)


# log something in console
class ConsoleLog(Statement):
    def __init__(self, output: Expression) -> None:
        self.output = output
    
    def __repr__(self) -> str:
        return f"ConsoleLog (console_log {self.output})"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, ConsoleLog):
            return NotImplemented
        
        return self.output == other.output
    
    def accept(self, visitor: StatementVisitor):
        return visitor.visit_console_log(self)
