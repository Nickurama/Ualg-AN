from sympy import *

class newton:
    @staticmethod
    def solve(x_values, y_values, error_margin):
        n = len(x_values)
        Q = [[0 for i in range(n)] for j in range(n)]

        for column in range(n):
            if column == 0:
                for i in range(n):
                    Q[i][0] = y_values[i]
            else:
                for row in range(n - column):
                    newton.Q_calc(Q, x_values, column + row, column)
        
        result = 0
        for i in range(n):
            result += Q[i][i] * newton.prod_calc(i, x_values)
        return result
    
    @staticmethod
    def Q_calc(Q, x_values, row, column):
        x0 = x_values[row - column]
        x1 = x_values[row]
        previous_Q_upper = Q[row - 1][column - 1]
        previous_Q_lower = Q[row][column - 1]
        Q[row][column] = (previous_Q_lower - previous_Q_upper) / (x1 - x0)
    
    @staticmethod
    def prod_calc(iteration, x_values):
        result = 1
        for i in range(iteration):
            result *= (symbols('x') - x_values[i])
        return result
