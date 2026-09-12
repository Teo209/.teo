from .expression import Expression


class Statement:
    pass


class ExpressionStatement(Statement):
    def __init__(self, expression: Expression) -> None:
        self.expression = expression


class Assignment(Statement):
    def __init__(self, name: str, value: Expression) -> None:
        self.name = name
        self.value = value


class ConsoleLog(Statement):
    def __init__(self, output: Expression) -> None:
        self.output = output
