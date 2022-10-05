from unicodedata import name


class calculator:

    def __init__(self,numberA,numberB) -> None:
        self.numberA = numberA
        self.numberB = numberB

    def add(self) -> int:
        return self.numberA + self.numberB
