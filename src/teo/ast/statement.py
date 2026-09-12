from .expression import Expression


class Statement:
    pass


class ExpressionStatement(Statement):
    def __init__(self, expression: Expression) -> None:
        self.expression = expression
    
    def __repr__(self) -> str:
        return f"ExpressionStatement (expression: {self.expression})"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, ExpressionStatement):
            return NotImplemented
        
        return self.expression == other.expression


class Assign(Statement):
    def __init__(self, name: str, value: Expression) -> None:
        self.name = name
        self.value = value
    
    def __repr__(self) -> str:
        return f"Assignment ({self.name} = {self.value})"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Assign):
            return NotImplemented
        
        return (
            self.name == other.name and
            self.value == other.value
        )

class ConsoleLog(Statement):
    def __init__(self, output: Expression) -> None:
        self.output = output
    
    def __repr__(self) -> str:
        return f"ConsoleLog (console_log {self.output})"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, ConsoleLog):
            return NotImplemented
        
        return self.output == other.output
