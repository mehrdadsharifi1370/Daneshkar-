# °F = (9/5 × °C) + 32
def CelsiusToFahrenheit(Celsius: int):
    return (((Celsius*9)/5)+32)


print(list(map(CelsiusToFahrenheit, (50, 60, 0))))
