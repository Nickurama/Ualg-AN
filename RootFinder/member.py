import re

class member:
    def __init__(self, coefficinet: float, exponent: float):
        self.coefficient = coefficinet
        self.exponent = exponent

    @classmethod
    def from_string(cls, str: str):
        coefficient = 1.0
        exponent = 1.0
        if "x" in str:
            coefficient_str = str[1:str.index("x")]
            exponent_str = str[str.index("x") + 1:len(str) - 1]
            if coefficient_str != '':
                coefficient = float(coefficient_str)
            if exponent_str != '':
                exponent = float(exponent_str)
        else:
            coefficient = float(str[1:len(str) - 1])
            exponent = 0.0

        return cls(coefficient, exponent)

    
    def calc(self, x: float) -> float:
        return self.coefficient * pow(x, self.exponent)
    
    def set_negative_coefficient(self):
        self.coefficient = self.coefficient * -1
