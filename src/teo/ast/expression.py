class Expression:
    pass


# literal
class Literal(Expression):
    def __init__(self, value) -> None:
        self.value = value
    
    def __repr__(self) -> str:
        return f"Literal (value: {self.value})"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Literal):
            return NotImplemented
        
        return self.value == other.value


# access variables
class Variable(Expression):
    def __init__(self, name) -> None:
        self.name = name
    
    def __repr__(self) -> str:
        return f"Variable (name: {self.name})"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Variable):
            return NotImplemented
        
        return self.name == other.name


# binary
class BinaryOperation(Expression):
    def __init__(self, left: Expression, operator, right: Expression) -> None:
        self.left = left
        self.operator = operator
        self.right = right
    
    def __repr__(self) -> str:
        return f"BinaryOperation (operation: {self.left} {self.operator} {self.right})"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, BinaryOperation):
            return NotImplemented
        
        return (
                self.left == other.left and
                self.operator == other.operator and
                self.right == other.right)


# unary
class UnaryOperation(Expression):
    def __init__(self, operator, right: Expression) -> None:
        self.operator = operator
        self.right = right
    
    def __repr__(self) -> str:
        return f"UnaryOperation (operation: {self.operator}{self.right})"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, UnaryOperation):
            return NotImplemented
        
        return (
            self.operator == other.operator and
            self.right == other.right)
