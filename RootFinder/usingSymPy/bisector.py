from sympy import *

class bisector:
    @staticmethod
    def get_half(x0, x1):
        return (x0 + x1) / 2
 
    @staticmethod
    def calc_root(expression, x0, x1, error_margin, iterations):
        half = bisector.get_half(x0, x1)

        if (abs(x1 - x0) <= error_margin):
            return half
        if (iterations <= 0):
            print("Reached max iterations, stopping.")
            return half

        if expression.subs(symbols("x"), half) == 0:
            return half
        elif expression.subs(symbols("x"), half) * expression.subs(symbols("x"), x0) < 0:
            return bisector.calc_root(expression, x0, half, error_margin, iterations - 1)
        elif expression.subs(symbols("x"), half) * expression.subs(symbols("x"), x1) < 0:
            return bisector.calc_root(expression, half, x1, error_margin, iterations - 1)
        else:
            if expression.subs(symbols("x"), x0) == 0:
                return x0
            elif  expression.subs(symbols("x"), x1) == 0:
                return x1
            else:
                raise Exception("Error: Unable to find roots with cauchy's theorem.")
        
    @staticmethod
    def calc_root_nonrecursive(expression, x0, x1, error_margin, iterations):
        
        half = bisector.get_half(x0, x1)
        while(abs(x1 - x0) > error_margin and iterations > 0):
            half = bisector.get_half(x0, x1)
            iterations -= 1
            if expression.subs(symbols("x"), half) == 0:
                return half
            elif expression.subs(symbols("x"), half) * expression.subs(symbols("x"), x0) < 0:
                x1 = half
            elif expression.subs(symbols("x"), half) * expression.subs(symbols("x"), x1) < 0:
                x0 = half
            else:
                if expression.subs(symbols("x"), x0) == 0:
                    return x0
                elif  expression.subs(symbols("x"), x1) == 0:
                    return x1
                raise Exception("Error! Unable to find roots with cauchy's theorem.")
        
        if (iterations <= 0):
            print("Reached max iterations, stopping.")
        
        return half