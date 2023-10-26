from sympy import *


class secant:
    @staticmethod
    def calc_root(expression, x0, x1, error_margin, iterations):
        startIterations = iterations
        new_x = x1 - (expression.subs(symbols("x"), x1) * (x1 - x0)) / (expression.subs(symbols("x"), x1) - expression.subs(symbols("x"), x0))

        while abs(new_x - x1) > error_margin and iterations > 0:
            if expression.subs(symbols("x"), new_x) == 0:
                print(f"Iterations: {int(startIterations - iterations)}")
                return new_x

            x0 = x1
            x1 = new_x
            iterations -= 1
            new_x = x1 - (expression.subs(symbols("x"), x1) * (x1 - x0)) / (expression.subs(symbols("x"), x1) - expression.subs(symbols("x"), x0))

        if iterations <= 0:
            print("Reached max iterations, stopping.")
        print(f"Iterations: {int(startIterations - iterations)}")

        return new_x
