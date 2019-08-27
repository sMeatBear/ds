import random as r


def fibonacci(n):
    a = b = 1
    print(a)
    for x in range(n):
        print(a)
        a, b = a + b, a
    # print("x: ", x)


def count_digit(n):
    digit = 0

    if n < 0:
        return 0

    while n > 1:
        n /= 10
        digit += 1
    return digit


def to_binary(decimal, scale=2):
    result = []
    res_str = ''
    quotient = None
    divident = decimal
    dividor = scale

    while quotient != 0:
        quotient = int(divident / dividor)
        result.append(divident % dividor)
        divident = quotient

    while result != []:
        res_str += str(result.pop())
        

    return int(res_str)


# print(count_digit(9068291961949055))
# fibonacci(5)
# print(r.sample(range(1, 34), 5))
print(to_binary(379))
