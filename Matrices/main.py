import math_input
import jacobi as my_jacobi
import gauss
from sympy import *

def print_approx(approximations, precision):
    for i in range(len(approximations)):
        print(f"x{i}: {round(approximations[i], precision)}")

exit = false
print("tip: Ctrl+C to exit!")
while exit == false:
    print(">------------------------------------<")
    try:
        precision = math_input.math_input.get_precision()
        num_variables = math_input.math_input.get_num_variables()
        # num_equations = math_input.math_input.get_num_equations(num_variables)
        rows = []
        for i in range(num_variables): # changed to num_variables
            rows.append(math_input.math_input.get_row(num_variables, i + 1, precision))
        equalities = math_input.math_input.get_equalities(num_variables, precision)
        matrix = Matrix(rows)
        equalities_matrix = Matrix(equalities)
        pprint(MatMul(matrix, equalities_matrix), use_unicode=False)
        error_margin = math_input.math_input.get_error_margin(precision)
        max_iterations = math_input.math_input.get_max_iterations(precision)
        try:
            print(">-- solve (Jacobi) --<")
            result_jacobi = my_jacobi.jacobi.solve(matrix, equalities, error_margin, max_iterations)
            print_approx(result_jacobi, precision)
        except Exception as e:
            print("Jacobi's method failed.")
            print(str(e))
        try:
            print(">-- solve (Gauss) --<")
            result_gauss = gauss.gauss.solve(matrix, equalities, error_margin, max_iterations)
            print_approx(result_gauss, precision)
        except Exception as e:
            print("Gauss's method failed.")
            print(str(e))
    except KeyboardInterrupt:
        exit = true
    except Exception as e:
        print(str(e))

print("")
print("Exiting...")
