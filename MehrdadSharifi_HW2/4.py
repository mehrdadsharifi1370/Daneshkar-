def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def neper_number_power(x, terms=100):
    result = 0
    for n in range(terms):
        result += (x ** n) / factorial(n)
    return result


# Example usage
x = float(input("Enter the value of x: "))
result = neper_number_power(x)
print(f"e raised to the power of {x} is approximately: {result}")
