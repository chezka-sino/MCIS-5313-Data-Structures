def isOperator(symbol):
    operators = ['+', '-', '*', '/']
    return symbol in operators


def reverseExpression(expression):
    expression = expression[len(expression)::-1]
    return [symbol for symbol in expression]


def postfixToInfix(expression):

    postfix = reverseExpression(expression)
    infix = []

    while len(postfix) > 0:
        symbol = postfix.pop()

        if not isOperator(symbol):
            infix.append(symbol)

        else:
            val1 = infix.pop()
            val2 = infix.pop()
            new_val = '(' + val2 + symbol + val1 + ')'
            infix.append(new_val)

    return ''.join(infix)


def testPostfixToInfix(expression, expected):
    print("Postfix expression:", expression)
    print("Expected Infix:", expected)
    print("Infix result:", postfixToInfix(expression))
    return


if __name__ == "__main__":
    test_expression = 'ABC*+DE/F*-'
    test_expected = '(A+(B*C))-((D/E)*F))'

    testPostfixToInfix(test_expression, test_expected)
    print()

    test_expression_2 = 'AB*CD/+'
    test_expected_2 = '((A*B)+(C/D))'
    testPostfixToInfix(test_expression_2, test_expected_2)
