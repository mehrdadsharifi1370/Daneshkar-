number = input()
res = 0


def sum_all(numbers: str):
    sum = 0
    numbers = str(numbers)
    for index in range(len(numbers)):
        sum = sum + int(numbers[index])
    return sum


res = sum_all(number)
while res >= 10:
    res = sum_all(res)
print(res)
