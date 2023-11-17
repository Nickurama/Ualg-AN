import math_input
import neville
import newton
from sympy import *

def get_max_len(values):
    max_len = 0
    for value in values:
        pretty_str = pretty(value, full_prec=False)
        if len(pretty_str) > max_len:
            max_len = len(pretty_str)
    return max_len

def print_values(x_values, y_values):
    max_len = max(get_max_len(x_values), get_max_len(y_values))
    print("<" + "-"*max_len*2 + ">")
    formatter = "{:<" + str(max_len) + "}"
    formatter += " {:<" + str(max_len) + "}"
    print(formatter.format('x', 'y'))
    for i in range(len(x_values)):
        print(formatter.format(pretty(x_values[i], full_prec=False), pretty(y_values[i], full_prec=False)))
    print("<" + "-"*max_len*2 + ">")


exit = false
print("tip: Ctrl+C to exit!")
while exit == false:
    print(">------------------------------------<")
    try:
        precision = math_input.math_input.get_precision()
        num_nodes = math_input.math_input.get_num_nodes()
        x_values = math_input.math_input.get_values(num_nodes, precision, "x")
        y_values = math_input.math_input.get_values(num_nodes, precision, "y")
        print_values(x_values, y_values)
        error_margin = math_input.math_input.get_error_margin(precision)
        try:
            print(">-- interpolation (Neville) --<")
            result_neville = neville.neville.solve(x_values, y_values, error_margin)
            pprint(simplify(result_neville), use_unicode=False)
        except Exception as e:
            print("Neville's method failed.")
            print(str(e))
        try:
            print(">-- interpolation (Newton) --<")
            result_newton = newton.newton.solve(x_values, y_values, error_margin)
            pprint(simplify(result_newton), use_unicode=False)
        except Exception as e:
            print("Newton's method failed.")
            print(str(e))
    except KeyboardInterrupt:
        exit = true
    except Exception as e:
        print(str(e))

print("")
print("Exiting...")
