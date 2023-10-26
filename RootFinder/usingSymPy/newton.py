from sympy import *

class newton:
    @staticmethod
    def calc_root(expression, x, error_margin, iterations):
        if (iterations <= 0):
            print("Reached max iterations, stopping.")
            return x
        if (expression.subs(symbols("x"), x) == 0):
            return x

        derivative = diff(expression, symbols("x"))

        if (derivative.subs(symbols("x"), x) == 0):
            print("Derivative was 0! Inflexion point found. Returning current value.")
            return x

        new_x = x - (expression.subs(symbols("x"), x) / derivative.subs(symbols("x"), x))

        if (abs(new_x - x) <= error_margin):
            return new_x
        
        return newton.calc_root(expression, new_x, error_margin, iterations - 1)
    
    @staticmethod
    def calc_root_nonrecursive(expression, x, error_margin, iterations):
        derivative = diff(expression, symbols("x"))

        new_x = x - (expression.subs(symbols("x"), x) / derivative.subs(symbols("x"), x))
        while(abs(new_x - x) > error_margin and iterations > 0):
            x = new_x
            if (expression.subs(symbols("x"), x) == 0):
                return x
            elif (derivative.subs(symbols("x"), x) == 0):
                print("Derivative was 0! Inflexion point found. Returning current value.")
                return x

            iterations -= 1
            new_x = x - (expression.subs(symbols("x"), x) / derivative.subs(symbols("x"), x))

        if (iterations <= 0):
            print("Reached max iterations, stopping.")

        return new_x
            










        
        return newton.calc_root(expression, new_x, error_margin, iterations - 1)