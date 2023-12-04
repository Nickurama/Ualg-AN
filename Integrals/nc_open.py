from sympy import *

class nc_open:
    @staticmethod
    def solve(expression, range0, range1):
        h = nc_open.calc_h(range0, range1)
        return (5 / 24) * h * (
            11 * expression.subs(Symbol("x"), nc_open.calc_x(range0, 0, h)) +
            expression.subs(Symbol("x"), nc_open.calc_x(range0, 1, h)) +
            expression.subs(Symbol("x"), nc_open.calc_x(range0, 2, h)) +
            11 * expression.subs(Symbol("x"), nc_open.calc_x(range0, 3, h)))

    @staticmethod
    def calc_h(range0, range1):
        return (range1 - range0) / 5

    @staticmethod
    def calc_x(range0, i, h):
        return range0 + (i + 1) * h

    @staticmethod
    def calc_error(expression, range0, range1):
        h = nc_open.calc_h(range0, range1)
        fourth_derivative = diff(expression, Symbol("x"), 4)
        max_diff_error = Abs(fourth_derivative.subs(Symbol("x"), nc_open.calc_x(range0, -1, h)))
        for i in range(5):
            max_diff_error = Max(max_diff_error, Abs(fourth_derivative.subs(Symbol("x"), nc_open.calc_x(range0, i, h))))
        return (95 / 144) * Pow(h, 5) * max_diff_error