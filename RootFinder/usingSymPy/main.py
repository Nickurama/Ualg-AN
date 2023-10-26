import bisector
import math_input
from sympy import *


exit = false
print(">------------------------------------<")
print("tip: Ctrl+C to exit!")
while (exit == false):
    print(">------------------------------------<")
    try:
        precision = math_input.math_input.get_precision()
        expression = math_input.math_input.get_expression(precision)
        range0 = math_input.math_input.get_range0(precision)
        range1 = math_input.math_input.get_range1(range0, precision)
        error_margin = math_input.math_input.get_error_margin(precision)
        max_iterations = math_input.math_input.get_max_iterations(precision)
        result = bisector.bisector.calc_root_nonrecursive(expression, range0, range1, error_margin, max_iterations)
        print(f"root: {round(result, precision)}")
    except KeyboardInterrupt:
        exit = true
    except Exception as e:
        print(str(e))

print("")
print("Exiting...")
print(">------------------------------------<")

