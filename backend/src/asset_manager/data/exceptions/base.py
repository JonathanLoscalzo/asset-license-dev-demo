

class ItemNotFound(Exception):
    message: str
    def __init__(self, id):
        self.id = id
        self.message = f"Item {id} not found"
        super().__init__(self.message)

class MethodShouldNotBeImplemented(Exception):
    def __init__(self, method:str):
        self.method = method
        super().__init__(f"Method {method} should not be implemented")