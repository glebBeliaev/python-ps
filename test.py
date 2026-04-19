def multiplyer(factor: float):
    def inner(x: float):
        return x * factor

    return inner


double = multiplyer(2)
triple = multiplyer(3)

print(double(10))
print(type(double))
print(triple(20))
