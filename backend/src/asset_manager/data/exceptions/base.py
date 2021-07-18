

class ItemNotFound(Exception):
    def __init__(self, id):
        self.id = id
        super().__init__(f"Item {id} not found")

class MethodShouldNotBeImplemented(Exception):
    def __init__(self, method:str):
        self.method = method
        super().__init__(f"Method {method} should not be implemented")