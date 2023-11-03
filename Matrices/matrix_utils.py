from sympy import *

class matrix_utils:
    @staticmethod
    def substitute_values(expression, values):
        for i in range(len(values)):
            expression = expression.subs(Symbol("x" + str(i)), values[i])
        return expression
        
    
    @staticmethod
    def get_expressions(matrix, equalities):
        expressions = []
        for i in range(matrix.rows):
            current_expression = equalities[i]
            current_diag = matrix[i, i]
            if current_diag == 0:
                raise Exception("Error: Invalid matrix. Diagonal should not contain zeros.")
            for j in range(matrix.cols):
                if i != j: # if not in the diagonal
                    current_expression += Symbol("x" + str(j)) * -1 * matrix[i, j]
            current_expression /= current_diag
            expressions.append(current_expression)
        return expressions
    
    @staticmethod
    def calc_error(approx, new_approx):
        error = 0
        for i in range(len(approx)):
            error += abs(new_approx[i] - approx[i])
        return error
