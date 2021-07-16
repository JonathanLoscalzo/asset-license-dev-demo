

class ItemNotFound(Exception):
    def __init__(self, id):
        self.id = id
        super().__init__(f"Item {id} not found")
