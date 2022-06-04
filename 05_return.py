def add_numbers(a, b):
    return a + b


def multiply_numbers(a, b):
    return a * b


def divide_numbers(a, b):
    return a / b
    # return a // b returns an int


add_result = add_numbers(10, 4)

multiply_result = multiply_numbers(add_result, 32)

final_result = divide_numbers(multiply_result, 40)

print(final_result)