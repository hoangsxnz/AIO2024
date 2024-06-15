import math

alpha = 0.01

# Given


def is_number(n):
    try:
        float(n)  # Type - casting the string to ‘float ‘.
        # If string is not a valid ‘float ‘ ,
        # it ’ll raise ‘ValueError ‘ exception
    except ValueError:
        return False
    return True


def calc_activation_function(x, activation_function):
    assert is_number(x), "x must be a number"

    x = float(x)
    print(f"Input x = {x}")
    print(
        f"Input activation Function (sigmoid|relu|elu): {activation_function}")

    if activation_function == 'relu':
        if x <= 0:
            print(f"relu: f({x}) = 0")
        else:
            print(f"relu: f({x}) = {x}")
    elif activation_function == 'sigmoid':
        print(f"sigmoid: f({x}) = {1 / (1 + math.exp(-x))}")
    elif activation_function == 'elu':
        if x <= 0:
            print(f"elu: f({x}) = {alpha * (math.exp(x)- 1)}")
        else:
            print(f"elu: f({x}) = {x}")
    else:
        print(f"{activation_function} is not supported")


calc_activation_function(1.5, 'elu')
