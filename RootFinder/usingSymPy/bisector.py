from sympy import *


class bisector:
    @staticmethod
    def get_half(x0: float, x1: float) -> float:
        return (x0 + x1) / 2
    
    @staticmethod
    def get_half_infinite(x0, x1):
        return (x0 + x1) / 2
    
    @staticmethod
    def get_zero(expression, x0: float, x1: float, error_margin: float, iterations: int) -> float:
        half = bisector.get_half(x0, x1)

        if (x1 - x0 <= error_margin):
            return half
        if (iterations <= 0):
            print("Reached max iterations, stopping.")
            return half

        if expression.subs(symbols("x"), half) == 0:
            return half
        elif expression.subs(symbols("x"), half) * expression.subs(symbols("x"), x0) < 0:
            return bisector.get_zero(expression, x0, half, error_margin, iterations - 1)
        elif expression.subs(symbols("x"), half) * expression.subs(symbols("x"), x1) < 0:
            return bisector.get_zero(expression, half, x1, error_margin, iterations - 1)
        else:
            raise Exception("Error! Unable to find roots with cauchy's theorem.")
        
    @staticmethod
    def get_zero_infinite(expression, x0, x1, error_margin, iterations):
        
        half = bisector.get_half_infinite(x0, x1)

        if (x1 - x0 <= error_margin):
            return half
        if (iterations <= 0):
            print("Reached max iterations, stopping.")
            return half

        if expression.subs(symbols("x"), half) == 0:
            return half
        elif expression.subs(symbols("x"), half) * expression.subs(symbols("x"), x0) < 0:
            return bisector.get_zero(expression, x0, half, error_margin, iterations - 1)
        elif expression.subs(symbols("x"), half) * expression.subs(symbols("x"), x1) < 0:
            return bisector.get_zero(expression, half, x1, error_margin, iterations - 1)
        else:
            raise Exception("Error! Unable to find roots with cauchy's theorem.")
        
    @staticmethod
    def get_zero_infinite_nonrecursive(expression, x0, x1, error_margin, iterations):
        
        half = bisector.get_half_infinite(x0, x1)
        while(x1 - x0 > error_margin and iterations > 0):
            half = bisector.get_half_infinite(x0, x1)
            if expression.subs(symbols("x"), half) == 0:
                done = true
                return half
            elif expression.subs(symbols("x"), half) * expression.subs(symbols("x"), x0) < 0:
                x1 = half
                iterations -= 1
            elif expression.subs(symbols("x"), half) * expression.subs(symbols("x"), x1) < 0:
                x0 = half
                iterations -= 1
            else:
                raise Exception("Error! Unable to find roots with cauchy's theorem.")
        
        if (iterations <= 0):
            print("Reached max iterations, stopping.")