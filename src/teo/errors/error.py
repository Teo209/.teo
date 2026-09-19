from ..sourcespan.sourcespan import SourceSpan


class Error(Exception):
    def __init__(self, message, span: SourceSpan = None):
        self.message = message
        self.span = span
        super().__init__(self.message, self.span)

    
    def __str__(self):
        if self.span:
            return f"{self.message} at {self.span.start}"
        
        return self.message
