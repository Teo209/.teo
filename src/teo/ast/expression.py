# visitor class
class ExpressionVisitor:
    def visit_literal(self, literal: "Literal"):
        ...
    
    def visit_variable(self, variable: "Variable"):
        ...
    
    def visit_binary_operation(self, binary_operation: "BinaryOperation"):
        ...
    
    def visit_unary_operation(self, unary_operation: "UnaryOperation"):
        ...


# base class for expressions
class Expression:
    def accept(self, visitor: ExpressionVisitor):
        pass


# literal
class Literal(Expression):
    def __init__(self, value: object):
        self.value = value
    
    def __repr__(self) -> str:
        return f"Literal (value: {self.value})"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Literal):
            return NotImplemented
        
        return self.value == other.value
    
    def accept(self, visitor: ExpressionVisitor):
        return visitor.visit_literal(self)


# access variables
class Variable(Expression):
    def __init__(self, name):
        self.name = name
    
    def __repr__(self) -> str:
        return f"Variable (name: {self.name})"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Variable):
            return NotImplemented
        
        return self.name == other.name
    
    def accept(self, visitor: ExpressionVisitor):
        return visitor.visit_variable(self)


# binary
class BinaryOperation(Expression):
    def __init__(self, left: Expression, operator, right: Expression):
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
    
    def accept(self, visitor: ExpressionVisitor):
        return visitor.visit_binary_operation(self)


# unary
class UnaryOperation(Expression):
    def __init__(self, operator, right: Expression):
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

    def accept(self, visitor: ExpressionVisitor):
        return visitor.visit_unary_operation(self)
