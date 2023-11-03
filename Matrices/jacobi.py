from sympy import *
import matrix_utils

class jacobi:
    @staticmethod
    def solve(matrix, equalities, error_margin, max_iterations):
        if matrix.det() == 0:
            raise Exception("Error: Matrix is impossible. Determinant is 0.")
        
        expressions = matrix_utils.matrix_utils.get_expressions(matrix, equalities)
        approximations = [0] * matrix.rows
        new_approx = []
        iterations = 0
        error = 0
        if iterations < max_iterations:
            for i in range(matrix.rows):
                new_approx.append(matrix_utils.matrix_utils.substitute_values(expressions[i], approximations))
            error = matrix_utils.matrix_utils.calc_error(approximations, new_approx)
            approximations = new_approx
            new_approx = []
            iterations += 1
        while (iterations < max_iterations and error > error_margin):
            for i in range(matrix.rows):
                new_approx.append(matrix_utils.matrix_utils.substitute_values(expressions[i], approximations))
            new_error = matrix_utils.matrix_utils.calc_error(approximations, new_approx)
            if (new_error > error):
                raise Exception("Error: Matrix diverges with Jacobi's method.")
            error = new_error
            approximations = new_approx
            new_approx = []
            iterations += 1


        if (iterations >= max_iterations):
            print("max iterations reached.")

        print(f"finished in {iterations} iterations.")

        return approximations
