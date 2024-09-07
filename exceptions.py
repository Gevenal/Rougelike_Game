class Impossible(Exception):
    # exception raised when an action is paradoxical 
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message
