import bisector
import newton
import secant
import math_input
from sympy import *


exit = false
print("tip: Ctrl+C to exit!")
while exit == false:
    print(">------------------------------------<")
    try:  # ONLY WORKS IF THERE IS ONE AND ONLY ONE ROOT INSIDE RANGE
        precision = math_input.math_input.get_precision()  # 0 < x <= 100
        expression = math_input.math_input.get_expression(precision)
        range0 = math_input.math_input.get_range0(precision)
        range1 = math_input.math_input.get_range1(range0, precision)
        error_margin = math_input.math_input.get_error_margin(precision)  # can be 0 (but should set max_iterations)
        max_iterations = math_input.math_input.get_max_iterations(precision)  # can be oo (but should set error_margin)
        try:
            print(">-- root (bisector) --<")
            result_bisector = bisector.bisector.calc_root(expression, range0, range1, error_margin, max_iterations)
            print(f"result: {round(result_bisector, precision)}")
        except Exception as e:
            print(str(e))
            print("Bisector method failed.")
        try:
            print(">-- root (Newton) --<")
            result_newton = newton.newton.calc_root( expression, (range0 + range1) / 2, error_margin, max_iterations)  # point is (range0 + range1) / 2
            print(f"result: {round(result_newton, precision)}")
        except:
            print("Newton's method failed.")
        try:
            print(">-- root (Secant) --<")
            result_newton = secant.secant.calc_root(expression, range0, range1, error_margin, max_iterations)
            print(f"result: {round(result_newton, precision)}")
        except Exception as e:
            print(str(e))
            print("Secant's method failed.")
    except KeyboardInterrupt:
        exit = true
    except Exception as e:
        print(str(e))

print("")
print("Exiting...")
