def sum(a, b):
    # returns the sum of the two numbers
    return a + b


def difference(a, b):
    # returns the difference of the two numbers
    return a - b


def product(a, b):
    # returns the product of the two numbers
    return a * b


def quotient(a, b):
    # returns the sum of the two numbers if possible
    # NOTE: if user inputs 0 as the second number, function will return "undefined"
    try:
        return a / b
    except ZeroDivisionError:
        return "undefined"


if __name__ == "__main__":
    # asks the user for two integers
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))

    # prints the results
    print('--------------------')
    print(x, '+', y, '=', sum(x, y))
    print(x, '-', y, '=', difference(x, y))
    print(x, '*', y, '=', product(x, y))
    print(x, "/", y, '=', quotient(x, y))
