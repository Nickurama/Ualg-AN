import bisector
from sympy import *


precision = 100
expression = N(input("expression: "), precision)
range0 = N(input("initial range: "), precision)
range1 = N(input("final range: "), precision)
error_margin = N(input("error margin: "), precision)
max_iterations = N(input("max iterations: "))

try:
    print(bisector.bisector.get_zero_infinite_nonrecursive(expression, range0, range1, error_margin, max_iterations))
except Exception as e:
    print(str(e))


# expression = sympify(input("expression: "))
# range0 = float(input("initial range: "))
# range1 = float(input("final range: "))
# error_margin = float(input("error margin: "))
# max_iterations = int(input("max iterations: "))

# try:
#     print("%.99f" % bisector.bisector.get_zero(expression, range0, range1, error_margin, max_iterations))
# except Exception as e:
#     print(str(e))

