from sympy import *
import matrix_utils

class gauss:
    @staticmethod
    def solve(matrix, equalities, error_margin, max_iterations):
        if matrix.det() == 0:
            raise Exception("Error: Matrix is impossible (or possible undetermined). Determinant is 0.")
        
        expressions = matrix_utils.matrix_utils.get_expressions(matrix, equalities)
        approximations = [0] * matrix.rows
        new_approx = []

        iterations = 0
        error = 0
        if iterations < max_iterations:
            new_approx = approximations.copy()
            for i in range(matrix.rows):
                new_approx[i] = matrix_utils.matrix_utils.substitute_values(expressions[i], new_approx)
            error = matrix_utils.matrix_utils.calc_error(approximations, new_approx)
            approximations = new_approx
            iterations += 1
        while (iterations < max_iterations and error > error_margin):
            new_approx = approximations.copy()
            for i in range(matrix.rows):
                new_approx[i] = matrix_utils.matrix_utils.substitute_values(expressions[i], new_approx)
            new_error = matrix_utils.matrix_utils.calc_error(approximations, new_approx)
            if (new_error > error):
                raise Exception("Error: Matrix diverges with Gauss's method. (use a diagonally dominant matrix)")
            error = new_error
            approximations = new_approx
            iterations += 1


        if (iterations >= max_iterations):
            print("max iterations reached.")

        print(f"finished in {iterations} iterations.")

        return approximations
