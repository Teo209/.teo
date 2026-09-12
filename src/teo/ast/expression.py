class Expression:
    pass

# literal
class Literal(Expression):
    def __init__(self, value) -> None:
        self.value = value


# access variables
class Variable(Expression):
    def __init__(self, name) -> None:
        self.name = name


# binary
class BinaryOperation(Expression):
    def __init__(self, left: Expression, operator, right: Expression) -> None:
        self.left = left
        self.operator = operator
        self.right = right


# unary
class UnaryOperation(Expression):
    def __init__(self, operator, right: Expression) -> None:
        self.operator = operator
        self.right = right
