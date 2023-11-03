from sympy import *

class bisector:
    @staticmethod
    def get_half(x0, x1):
        return (x0 + x1) / 2

    @staticmethod
    def calc_root(expression, x0, x1, error_margin, iterations):
        startIterations = iterations
        half = bisector.get_half(x0, x1)
        while(abs(x1 - x0) > error_margin and iterations > 0):
            half = bisector.get_half(x0, x1)
            iterations -= 1
            if expression.subs(symbols("x"), half) == 0:
                print(f"Iterations: {int(startIterations - iterations)}")
                return half
            elif expression.subs(symbols("x"), half) * expression.subs(symbols("x"), x0) < 0:
                x1 = half
            elif expression.subs(symbols("x"), half) * expression.subs(symbols("x"), x1) < 0:
                x0 = half
            else:
                if expression.subs(symbols("x"), x0) == 0:
                    print(f"Iterations: {int(startIterations - iterations)}")
                    return x0
                elif  expression.subs(symbols("x"), x1) == 0:
                    print(f"Iterations: {int(startIterations - iterations)}")
                    return x1
                raise Exception("Error! Unable to find roots with cauchy's theorem.")
        
        if (iterations <= 0):
            print("Reached max iterations, stopping.")
        print(f"Iterations: {int(startIterations - iterations)}")
        
        return half