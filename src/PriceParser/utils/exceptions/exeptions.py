#Except if there is something not found
class NotFound(Exception):
    def __init__(self, message="This model was not found!"):
        self.message = message
        super().__init__(self.message)