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
    def get_num_nodes():
        this_input = input("number of nodes: ")
        try:
            try:
                this_input = int(this_input)
            except:
                raise Exception("Error: number of nodes must be an integer.")
            if this_input <= 0:
                raise Exception("Error: number of nodes should be a number greater than zero.")
            return this_input
        except Exception as e:
            raise e

    @staticmethod
    def get_values(num_nodes, precision, value_name):
        values = [];
        this_input = input(f"{value_name} values: ")
        try:
            tokens = this_input.split(" ")
            if len(tokens) != num_nodes:
                raise Exception(f"Error: expected {num_nodes} variables but got {len(tokens)}.")
            for token in tokens:
                value = N(token, precision)
                if not ask(Q.real(value)):
                    raise Exception(f"Error: Invalid node '{token}'.")
                values.append(value)
            return values
        except Exception as e:
            raise e
        
    @staticmethod
    def get_x_value(precision):
        this_input = input(f"x=")
        try:
            value = N(this_input, precision)
            if not ask(Q.real(value)):
                raise Exception(f"Error: Invalid x value '{value}'.")
            return value
        except Exception as e:
            raise e