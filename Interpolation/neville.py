from sympy import *

class neville:
    @staticmethod
    def solve(x_values, y_values):
        n = len(x_values)
        Q = [[0 for i in range(n)] for j in range(n)]

        for column in range(n):
            if column == 0:
                for i in range(n):
                    Q[i][0] = y_values[i]
            else:
                for row in range(n - column):
                    neville.Q_calc(Q, x_values, symbols('x'), column + row, column)
        return Q[n - 1][n - 1]
    
    @staticmethod
    def Q_calc(Q, x_values, value, row, column):
        x0 = x_values[row - column]
        x1 = x_values[row]
        previous_Q_upper = Q[row - 1][column - 1]
        previous_Q_lower = Q[row][column - 1]
        Q[row][column] = ((value - x0)*previous_Q_lower - (value - x1)*previous_Q_upper) / (x1 - x0)
