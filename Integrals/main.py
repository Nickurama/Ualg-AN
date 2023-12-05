import math_input
import nc_closed
import nc_open
from sympy import *

exit = false
print("tip: Ctrl+C to exit!")
while exit == false:
    print(">------------------------------------<")
    try:
        precision = math_input.math_input.get_precision()
        expression = math_input.math_input.get_expression(precision)
        range0 = math_input.math_input.get_range0(precision)
        range1 = math_input.math_input.get_range1(range0, precision)
        try:
            print(">-- Integration (Newton-Cotes Closed: n=4) --<")
            result = nc_closed.nc_closed.solve(expression, range0, range1)
            error = nc_closed.nc_closed.calc_error(expression, range0, range1)
            print(f"result: {round(result, precision)}")
            print(f"error: ±{round(error, precision)}")
        except Exception as e:
            print("Newton-Cotes Closed method failed.")
            print(str(e))
        try:
            print(">-- Integration (Newton-Cotes Open: n=3) --<")
            result = nc_open.nc_open.solve(expression, range0, range1)
            error = nc_open.nc_open.calc_error(expression, range0, range1)
            print(f"result: {round(result, precision)}")
            print(f"error: ±{round(error, precision)}")
        except Exception as e:
            print("Newton-Cotes Open method failed.")
            print(str(e))
    except KeyboardInterrupt:
        exit = true
    except Exception as e:
        print(str(e))

print("")
print("Exiting...")
