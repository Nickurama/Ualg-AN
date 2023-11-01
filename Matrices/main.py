import math_input
import jacobi
import gauss
from sympy import *

exit = false
print("tip: Ctrl+C to exit!")
while exit == false:
    print(">------------------------------------<")
    try:
        precision = math_input.math_input.get_precision()
        num_variables = math_input.math_input.get_num_variables()
        num_equations = math_input.math_input.get_num_equations(num_variables)
        rows = []
        for i in range(num_equations):
            rows.append(math_input.math_input.get_row(num_variables, i + 1, precision))
        equalities = math_input.math_input.get_equalities(num_variables, precision)
        matrix = Matrix(rows)
        equalities_matrix = Matrix(equalities)
        pprint(MatMul(matrix, equalities_matrix), use_unicode=False)
        error_margin = math_input.math_input.get_error_margin(precision)
        max_iterations = math_input.math_input.get_max_iterations(precision)
        try:
            print(">-- solve (Jacobi) --<")
            result_jacobi = jacobi.jacobi.solve(matrix, equalities, error_margin, max_iterations)
            print(f"result: {round(result_jacobi, precision)}")
        except:
            print("Jacobi's method failed.")
        try:
            print(">-- solve (Gauss) --<")
            result_gauss = gauss.gauss.solve(matrix, equalities, error_margin, max_iterations)
            print(f"result: {round(result_gauss, precision)}")
        except Exception as e:
            print(str(e))
            print("Gauss's method failed.")
    except KeyboardInterrupt:
        exit = true
    except Exception as e:
        print(str(e))

print("")
print("Exiting...")
