from sympy import *

class nc_closed:
    @staticmethod
    def solve(expression, range0, range1):
        h = nc_closed.calc_h(range0, range1)
        return (2 / 45) * h * (
            7 * expression.subs(Symbol("x"), nc_closed.calc_x(range0, 0, h)) +
            32 * expression.subs(Symbol("x"), nc_closed.calc_x(range0, 1, h)) +
            12 * expression.subs(Symbol("x"), nc_closed.calc_x(range0, 2, h)) +
            32 * expression.subs(Symbol("x"), nc_closed.calc_x(range0, 3, h)) +
            7 * expression.subs(Symbol("x"), nc_closed.calc_x(range0, 4, h)))

    @staticmethod
    def calc_h(range0, range1):
        return (range1 - range0) / 4

    @staticmethod
    def calc_x(range0, i, h):
        return range0 + i * h

    @staticmethod
    def calc_error(expression, range0, range1):
        h = nc_closed.calc_h(range0, range1)
        sixth_derivative = diff(expression, Symbol("x"), 6)
        max_diff_error = Abs(sixth_derivative.subs(Symbol("x"), nc_closed.calc_x(range0, 0, h)))
        for i in range(4):
            max_diff_error = Max(max_diff_error, Abs(sixth_derivative.subs(Symbol("x"), nc_closed.calc_x(range0, i + 1, h))))
        return (8 / 945) * Pow(h, 7) * max_diff_error