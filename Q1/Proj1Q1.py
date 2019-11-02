def isOperator(symbol):
    return

def reverse(expression):
    expression = expression[len(expression)::-1]
    print(expression)
    return

def postfixToInfix(expression):
    expression = expression[len(expression)::-1]
    print(expression)
    # postfix = self.expression.reverse()
    infix = []

    # print(postfix)
    return infix

def testPostfixToInfix(expression, expected):
    print("Postfix expression:", expression)
    print("Expected Infix:", expected)
    print("Infix result: TODO")

    return


if __name__ == "__main__":
    test_expression = 'ABC*+DE/F*-'
    test_expected = '(A+(B*C))+((D/E)*F))'

    testPostfixToInfix(test_expression, test_expected)
