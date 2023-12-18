import math_input
import newton
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
        equations = []
        for i in range(num_variables):
            equations.append(math_input.math_input.get_expression(precision))
        initial_values = math_input.math_input.get_initial_values(num_variables, precision)
        error_margin = math_input.math_input.get_error_margin(precision)
        max_iterations = math_input.math_input.get_max_iterations(precision)
        try:
            print(">-- solve (Newton's method) --<")
            result = newton.newton.solve(equations, initial_values, error_margin, max_iterations)
            newton.newton.print_result(result)
        except Exception as e:
            print("Newton's method failed.")
            print(str(e))
    except KeyboardInterrupt:
        exit = true
    except Exception as e:
        print(str(e))

print("")
print("Exiting...")
