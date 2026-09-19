class SourcePosition:
    def __init__(self, line, column):
        self.line = line
        self.column = column
    
    def __repr__(self):
        return f"line {self.line}, column {self.column}"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, SourcePosition):
            return NotImplemented
        
        return (
            self.line == other.line and
            self.column == other.column
        )


class SourceSpan:
    def __init__(self, start: SourcePosition, end: SourcePosition):
        self.start = start
        self.end = end
    
    def __repr__(self):
        return (f"{self.start.line}:{self.start.column}-{self.end.line}:{self.end.column}")
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, SourceSpan):
            return NotImplemented
        
        return (
            self.start == other.start and
            self.end == other.end
        )