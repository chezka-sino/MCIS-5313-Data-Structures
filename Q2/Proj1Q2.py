def isOperator(symbol):
    operators = ['+', '-', '*', '/']
    return symbol in operators

def isParenthesis(symbol):
    par = ['(',')']
    return symbol in par

def infixToPostfix(expression):
    return

def testInfixToPostfix(expression, expected):
    print("Infix expression:", expression)
    print("Expected Infix:", expected)
    print("Postfix result:", infixToPostfix(expression))
    return

if __name__ == "__main__":
    test_expression = ""
    test_expected = ""
    testInfixToPostfix(test_expression, test_expected)