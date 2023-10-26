import bisector
import math_input
from sympy import *


exit = false
print(">------------------------------------<")
print("tip: Ctrl+C to exit!")
while (exit == false):
    print(">------------------------------------<")
    try:
        precision = math_input.math_input.get_precision() # 0 < x <= 100
        expression = math_input.math_input.get_expression(precision) # pi / E / x^n / n*n / n+n / n-n / n/n
        range0 = math_input.math_input.get_range0(precision)
        range1 = math_input.math_input.get_range1(range0, precision) # range1 > range0 && função tem de ser contínua [range0, range1]
        error_margin = math_input.math_input.get_error_margin(precision) # can be 0 (but should set max_iterations)
        max_iterations = math_input.math_input.get_max_iterations(precision) # can be oo (but should set error_margin)
        result = bisector.bisector.calc_root_nonrecursive(expression, range0, range1, error_margin, max_iterations)
        print(f"root: {round(result, precision)}") # rounded to precision
    except KeyboardInterrupt:
        exit = true
    except Exception as e:
        print(str(e))

print("")
print("Exiting...")
print(">------------------------------------<")

