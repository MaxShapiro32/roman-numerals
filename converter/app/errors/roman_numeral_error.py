class InvalidRomanNumeralException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.errors = "Invalid Roman Numeral Exception"
        print(self.errors)

class InvalidNumberException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.errors = "Invalid Number Exception"
        print(self.errors)
