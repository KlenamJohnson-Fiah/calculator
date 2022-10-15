from unicodedata import name


class calculator:
    def __init__(self, numberA, numberB) -> None:
        self.numberA = numberA
        self.numberB = numberB

    def add(self) -> int:
        return self.numberA + self.numberB

    def addingDecimals(self) -> float:
        return self.numberA + self.numberB

    def multiplication(self) -> float:
        return self.numberA * self.numberB
