from teo.lexer.lexer import Token, TokenTypes
from teo.ast.expression import (
    Expression,
    Literal,
    Variable,
    BinaryOperation,
    UnaryOperation
)
from teo.ast.statement import (
    Statement,
    ExpressionStatement,
    Assign,
    ConsoleLog
)


class Parser:
    def __init__(self, token_list: list[Token]):
        self.token_list = token_list
        self.current = 0
        
        
    def parse(self) -> list[Statement]:
        # parse all
        
        result = []
        
        while True:
            next_token = self.peek()
            
            while next_token.type in [TokenTypes.NEWLINE, TokenTypes.SEMICOLON]:
                self.consume()
                next_token = self.peek()
            
            if next_token.type == TokenTypes.EOF:
                return result

            statement = self.parse_statement()
            result.append(statement)
            
            next_token = self.peek()
            if not next_token.type in [TokenTypes.NEWLINE, TokenTypes.SEMICOLON, TokenTypes.EOF]:
                raise SyntaxError (f"Missing \';\' after statement at line {next_token.line}")

    
    def parse_statement(self) -> Statement:
        # console_log a; a = 5; var a = 5
        
        next = self.peek()
        
        match next.type:
            case TokenTypes.VAR:
                self.consume()                                          # var
                next = self.peek()                                      # identifier
                
                if next.type != TokenTypes.IDENTIFIER:
                    raise SyntaxError(f"Expected identifier after 'var' at line {next.line}")
                
                token = self.consume()                                  # identifier
                next = self.peek()                                      # assign
                
                if next.type != TokenTypes.ASSIGN:
                    raise SyntaxError(f"Expected '=' after var {token} at line {next.line}")
                
                self.consume()                                          # assign
                    
                expr = self.parse_expression()                          # value

                return Assign(token.value, expr, is_local=True)
            
            case TokenTypes.CONSOLE_LOG:
                token = self.consume()                                  # console_log
                expr = self.parse_expression()                          # value
                
                return ConsoleLog(expr)
            
            case TokenTypes.IDENTIFIER:
                next = self.peek_next()                                 # assign
                
                if next.type != TokenTypes.ASSIGN:
                    return ExpressionStatement(self.parse_expression()) # value
                
                token = self.consume()                                  # identifier
                self.consume()                                          # assign
                    
                expr = self.parse_expression()                          # value

                return Assign(token.value, expr)
            
            case _:
                return ExpressionStatement(self.parse_expression())     # value
        
    
    def parse_expression(self) -> Expression:
        # a + 1
        
        result = self.parse_addition()

        return result

    
    def parse_addition(self) -> Expression:
        # + -
        
        left = self.parse_multiplication()
        
        while self.peek().type in [TokenTypes.PLUS, TokenTypes.MINUS]:
            operator = self.consume()
            
            right = self.parse_multiplication()
            
            left = BinaryOperation(left, operator.value, right)
        
        return left


    def parse_multiplication(self) -> Expression:
        # * /
        
        left = self.parse_unary()
        
        while self.peek().type in [TokenTypes.MULTIPLY, TokenTypes.DIVIDE]:
            operator = self.consume()
            
            right = self.parse_unary()
            
            left = BinaryOperation(left, operator.value, right)
        
        return left
    
    
    def parse_unary(self) -> Expression:
        # Unary: -5 +5 -+5 --5 etc
        
        next_token = self.peek()
        
        match next_token.type:
            case TokenTypes.MINUS:
                self.consume()
                result = UnaryOperation("-", self.parse_unary())
            case TokenTypes.PLUS:
                self.consume()
                result = UnaryOperation("+", self.parse_unary())
            case _: 
                result = self.parse_primary()
        
        return result
    
    
    def parse_primary(self) -> Expression:
        # Number, Identifier
        
        if self.peek().type == TokenTypes.EOF:
            raise SyntaxError(f"End of file, expected token at line {self.peek().line}")
        
        token = self.consume()
        
        match token.type:
            case TokenTypes.NUMBER:
                result = Literal(int(token.value))
            case TokenTypes.IDENTIFIER:
                result = Variable(token.value)
            case _:
                result = None
                raise SyntaxError(f"Invalid token {token} at line {token.line}")
            
        return result
        
        
    def consume(self) -> Token:
        # return current token and increase counter
        
        token = self.token_list[self.current]
        self.current += 1
        
        return token

    def peek(self) -> Token:
        # return current token
        
        token = self.token_list[self.current]
        
        return token
    
    
    def peek_next(self) -> Token:
        # return the next token
        
        token = self.token_list[self.current + 1]
        
        return token
