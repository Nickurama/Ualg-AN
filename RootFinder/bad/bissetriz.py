import polynomial as Polynomial


class bissetriz:

    @staticmethod
    def get_half(x0: float, x1: float) -> float:
        return (x0 + x1) / 2

    @staticmethod
    def get_zero(poly: Polynomial, x0: float, x1: float, error_margin: float) -> float:
        half = bissetriz.get_half(x0, x1)
        
        if x1 - x0 <= error_margin:
            return half
        
        if poly.calc(half) == 0:
            return half
        elif poly.calc(half) * poly.calc(x0) < 0:
            return bissetriz.get_zero(poly, x0, half, error_margin)
        else:
            return bissetriz.get_zero(poly, half, x1, error_margin)
        

    
