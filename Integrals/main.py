import math_input
import nc_closed
import nc_open
from sympy import *
import math

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
            error = None
            try:
                error = nc_closed.nc_closed.calc_error(expression, range0, range1)
            except Exception as e:
                print("could not calculate error.")
            if (math.isnan(result)):
                raise Exception()
            print(f"result: {round(result, precision)}")
            try:
                print(f"error: ±{round(error, precision)}")
            except Exception as e:
                pass
        except Exception as e:
            print("Newton-Cotes Closed method failed.")
            print("Is the expression continuous in the given range?")
            print(str(e))
        try:
            print(">-- Integration (Newton-Cotes Open: n=3) --<")
            result = nc_open.nc_open.solve(expression, range0, range1)
            error = None
            try:
                error = nc_closed.nc_closed.calc_error(expression, range0, range1)
            except Exception as e:
                print("could not calculate error.")
            print(f"result: {round(result, precision)}")
            try:
                print(f"error: ±{round(error, precision)}")
            except Exception as e:
                pass
        except Exception as e:
            print("Newton-Cotes Open method failed.")
            print("Is the expression continuous in the given range?")
            print(str(e))
    except KeyboardInterrupt:
        exit = true
    except Exception as e:
        print(str(e))

print("")
print("Exiting...")
