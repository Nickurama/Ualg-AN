from sympy import *

class math_input:
    @staticmethod
    def get_precision():
        this_input = input("precision: ")
        try:
            this_input = N(this_input)
            if (ask(Q.integer(this_input))):
                raise Exception("Error: precision must be an integer.")
            if (this_input < 0 or this_input > 100):
                raise Exception("Error: Precision must be between 0 and 100.")
            return int(this_input)
        except Exception as e:
            raise e

    @staticmethod
    def get_expression(precision):
        this_input = input("expression: ")
        try:
            return N(this_input, precision)
        except:
            raise Exception("Error: Invalid expression: '" + this_input + "'.")
    
    @staticmethod
    def get_range0(precision):
        this_input = input("initial range: ")
        try:
            this_input = N(this_input, precision)
            if (not ask(Q.real(this_input))):
                raise Exception()
            return this_input
        except:
            raise Exception("Error: Invalid range.")
        
    @staticmethod
    def get_range1(range0, precision):
        this_input = input("final range: ")
        try:
            this_input = N(this_input, precision)
        except:
            raise Exception("Error: Invalid range.")
        try:
            if (not ask(Q.real(this_input))):
                raise Exception("Error: Invalid range.")
            elif (range0 >= this_input):
                raise Exception("Error: final range should be greater than initial range.")
            return this_input
        except Exception as e:
            raise e
    
    @staticmethod
    def get_error_margin(precision):
        this_input = input("error margin: ")
        try:
            this_input = N(this_input, precision)
            if (not ask(Q.real(this_input))):
                raise Exception("Error: Invalid error margin.")
            return this_input
        except Exception as e:
            raise e
    
    @staticmethod
    def get_max_iterations(precision):
        this_input = input("max iterations: ")
        try:
            this_input = N(this_input, precision)
            if (not ask(Q.real(this_input)) and not ask(Q.positive_infinite(this_input))):
                raise Exception("Error: Invalid maximum iterations.")
            return this_input
        except Exception as e:
            raise e