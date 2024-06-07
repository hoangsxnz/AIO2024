def factorial(n):
    res = 1
    for i in range(2, n+1):
        res *= i
    return res

def approx_sin(x, n):
    res = 0
    for i in range(n):
        coefficient = (-1)**i
        numerator = x**(2*i + 1)
        denominator = factorial(2*i + 1)
        tmp = coefficient*(numerator/denominator)
        res += tmp
    return res

def approx_cos(x, n):
    res = 0
    for i in range(n):
        coefficient = (-1)**i
        numerator = x **(2*i)
        denominator = factorial(2*i)
        tmp = coefficient*(numerator/denominator)
        res += tmp
    return res

def approx_sinh(x, n):
    res = 0
    for i in range(n):
        numerator = x**(2*i+1)
        denominator = factorial(2*i + 1)
        tmp = (numerator/denominator)
        res += tmp
    return res

def approx_cosh(x, n):
    res = 0
    for i in range(n):
        numerator = x**(2*i)
        denominator = factorial(2*i)
        tmp = (numerator / denominator)
        res += tmp
    return res