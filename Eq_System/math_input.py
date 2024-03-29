from sympy import *

class math_input:
    @staticmethod
    def get_precision():
        this_input = input("precision: ")
        try:
            try:
                this_input = int(this_input)
            except:
                raise Exception("Error: precision must be an integer.")
            if not ask(Q.integer(this_input)):
                raise Exception("Error: precision must be an integer.")
            if this_input < 0 or this_input > 100:
                raise Exception("Error: Precision must be between 0 and 100.")
            return int(this_input)
        except Exception as e:
            raise e

    @staticmethod
    def get_num_variables():
        this_input = input("number of variables: ")
        try:
            try:
                this_input = int(this_input)
            except:
                raise Exception("Error: number of variables must be an integer.")
            if this_input <= 0:
                raise Exception("Error: number of variables should be a number greater than zero.")
            return this_input
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
    def get_initial_values(num_variables, precision):
        row = []
        this_input = input("starting values: ")
        try:
            tokens = this_input.split(" ")
            if len(tokens) != num_variables:
                raise Exception(f"Error: expected {num_variables} values but got {len(tokens)}.")
            for token in tokens:
                cell = N(token, precision)
                if not ask(Q.real(cell)):
                    raise Exception(f"Error: Invalid value '{token}'.")
                row.append(N(token, precision))
            return row
        except Exception as e:
            raise e
    
    @staticmethod
    def get_error_margin(precision):
        this_input = input("error margin: ")
        try:
            this_input = N(this_input, precision)
            if not ask(Q.real(this_input)):
                raise Exception("Error: Invalid error margin.")
            if ask(Q.negative(this_input)):
                raise Exception("Error: Margin should be positive.")
            return this_input
        except Exception as e:
            raise e

    @staticmethod
    def get_max_iterations(precision):
        this_input = input("max iterations: ")
        try:
            this_input = N(this_input, precision)
            if not ask(Q.real(this_input)) and not ask(Q.positive_infinite(this_input)):
                raise Exception("Error: Invalid maximum iterations.")
            if ask(Q.negative(this_input)):
                raise Exception("Error: iterations should be positive.")
            return this_input
        except Exception as e:
            raise e