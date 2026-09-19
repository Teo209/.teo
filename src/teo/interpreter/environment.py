from teo.errors.runtime import TeoRuntimeError


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
        # Return True if variable is found and value can be assigned else define it and return False

        environment = self.find(name)

        if environment:
            environment.values[name] = value
            return True

        self.define(name, value)
        return False
    
    
    def get(self, name: str) -> object:
        # Return variable value
        # Return variable value if it is found else raises error
        
        environment = self.find(name)
        
        if not environment:
            raise TeoRuntimeError(f"Variable {name} not found")
        
        return environment.values[name]
    

    def find(self, name: str):
        if name in self.values:
            return self

        if self.enclosing:
            return self.enclosing.find(name)

        return None
    
    def __repr__(self):
        return f"Environment (enclosing: {str(self.enclosing)}, \nvalues = {self.values})"
