from sympy import *

class newton:
    @staticmethod
    def solve(equations, values, error_margin, max_iterations):
        if (max_iterations == 0):
            return values
        J = newton.calc_jacobian(equations)
        X = Matrix(values)
        eq_matrix = Matrix(equations)
        F = newton.subs_matrix(eq_matrix, values)

        iteration_J = newton.subs_matrix(J, values).inv()
        result = X - iteration_J * F

        print("Jacobian:")
        pprint(J)


        old_values = values.copy()
        for i in range(len(values)):
            values[i] = result[i]
        
        iteration = 1
        error = newton.calc_error(old_values, values)
        last_error = 0
        while(iteration < max_iterations and error > error_margin):
            X = Matrix(values)
            F = newton.subs_matrix(eq_matrix, values)
            iteration_J = newton.subs_matrix(J, values).inv()
            result = X - iteration_J * F

            old_values = values.copy()
            for i in range(len(values)):
                values[i] = result[i]

            iteration += 1
            last_error = error
            error = newton.calc_error(old_values, values)

            if (last_error < error):
                print("WARNING: diverging result detected! (maybe the initial values aren't close enough to the solution?)")
                break
        
        print(f"finished in {iteration} iterations")
        if (iteration >= max_iterations):
            print("max iterations reached.")
        if (error <= error_margin):
            print("error margin reached.")

        return values
    
    @staticmethod
    def calc_jacobian(equations):
        rows = []
        for row in range(len(equations)):
            cols = []
            for col in range(len(equations)):
                cols.append(diff(equations[row], Symbol("x" + str(col))))
            rows.append(cols)
        return Matrix(rows)

    @staticmethod
    def subs_matrix(matrix, values):
        rows = []
        for row in range(matrix.rows):
            cols = []
            for col in range(matrix.cols):
                cell = matrix[row, col]
                for valueIndex in range(len(values)):
                    cell = cell.subs(Symbol("x" + str(valueIndex)), values[valueIndex])
                cols.append(cell)
            rows.append(cols)
        return Matrix(rows)

    @staticmethod
    def calc_error(old_values, values):
        error = 0
        errors = []
        for i in range(len(old_values)):
            errors.append(abs(values[i] - old_values[i]))
        error = max(errors)
        return error
    
    @staticmethod
    def print_result(result):
        for i in range(len(result)):
            print("x" + str(i) + "=" + str(result[i]))
