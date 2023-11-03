from sympy import *

class newton:
    @staticmethod
    def calc_root(expression, x, error_margin, iterations):
        startIterations = iterations
        derivative = diff(expression, symbols("x"))

        new_x = x - (expression.subs(symbols("x"), x) / derivative.subs(symbols("x"), x))
        while(abs(new_x - x) > error_margin and iterations > 0):
            x = new_x
            if (expression.subs(symbols("x"), x) == 0):
                print(f"Iterations: {int(startIterations - iterations)}")
                return x
            elif (derivative.subs(symbols("x"), x) == 0):
                print("Derivative was 0! Inflexion point found. Returning current value.")
                print(f"Iterations: {int(startIterations - iterations)}")
                return x

            iterations -= 1
            new_x = x - (expression.subs(symbols("x"), x) / derivative.subs(symbols("x"), x))

        if (iterations <= 0):
            print("Reached max iterations, stopping.")
        print(f"Iterations: {int(startIterations - iterations)}")

        return new_x
