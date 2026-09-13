class Environment:
    def __init__(self, enclosing: "Environment | None" = None):
        # Global space
        self.enclosing = enclosing
        
        # Local space
        self.values: dict[str, object] = {}
    
    
    def define(self, name: str, value: object) -> bool:
        # Define a variable
        # Return False if variable already exists else True if defined successfully
        
        if name in self.values:
            return False

        self.values[name] = value
        
        return True
    
    
    def assign(self, name: str, value: object) -> bool:
        # Give a value to a variable
        # Return True if variable is found and value can be assigned else False
        
        if name in self.values:
            self.values[name] = value
            return True
        
        if self.enclosing:
            return self.enclosing.assign(name, value)
        
        raise NameError(f"Variable {name} not found")
    
    
    def get(self, name: str) -> object:
        # Return variable value
        # Return variable value if it is found else raises error
        
        if name in self.values:
            return self.values[name]
        
        if self.enclosing:
            return self.enclosing.get(name)
        
        raise NameError(f"Variable {name} not found")
