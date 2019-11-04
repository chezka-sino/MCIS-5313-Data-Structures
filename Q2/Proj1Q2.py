def isOperator(symbol):
    operators = ['+', '-', '*', '/', '(', ')']
    return symbol in operators

def isOperand(symbol):
    return symbol.isalpha()

def isLeftParenthesis(symbol):
    return symbol == '('

def isRightParenthesis(symbol):
    return symbol == ')'

def reverseExpression(expression):
    expression = '(' + expression + ')'
    print(expression)
    expression = expression[len(expression)::-1]
    return [symbol for symbol in expression]

def hierarchy(symbol):
    # TODO hierarchy check for operands
    switcher = {
        '*': 2,
        '/': 2,
        '+': 1,
        '-': 1
    }

    return switcher.get(symbol)

def infixToPostfix(expression):
    # TODO infix to postfix converter
    infix = reverseExpression(expression)
    operatorStack = []
    postfix = []

    while len(infix) > 0:
        symbol = infix.pop()

        if isOperand(symbol):
            postfix.append(symbol)

        if isLeftParenthesis(symbol):
            operatorStack.append(symbol)

        if isRightParenthesis(symbol):
            topOperator = operatorStack.pop()

            while not isLeftParenthesis(topOperator):
                postfix.append(topOperator)
                topOperator = operatorStack.pop()

        if isOperator(symbol):
            print('operator', symbol)
            print(operatorStack)

    return ''.join(postfix)

def testInfixToPostfix(expression, expected):
    print("Infix expression:", expression)
    print("Expected Infix:", expected)
    print("Postfix result:", infixToPostfix(expression))
    return

if __name__ == "__main__":
    test_expression = "(A+(B*C))+((D/E)*F)"
    test_expected = ""
    testInfixToPostfix(test_expression, test_expected)
    # print(hierarchy('-') <= hierarchy('+'))
    # print(isLeftParenthesis('('))