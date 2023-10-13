import polynomial as Polynomial
import bissetriz as Bissetriz

poly = Polynomial.polynomial.from_string(input("polynomial: "))
range0 = float(input("initial range: "))
range1 = float(input("final range: "))
error_margin = float(input("error margin: "))

print(Bissetriz.bissetriz.get_zero(poly, range0, range1, error_margin))