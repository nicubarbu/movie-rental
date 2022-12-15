class DuplicateError(Exception):
    def __init__(self, input):
        self.__input = input
        
    def __str__(self):
        return f'DuplicateError: {self.__input}'