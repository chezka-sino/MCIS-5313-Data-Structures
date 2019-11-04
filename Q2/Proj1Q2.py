def isOperator(symbol):
    # checks if symbol is an operator
    operators = ['+', '-', '*', '/']
    return symbol in operators

def isOperand(symbol):
    # checks if symbol is an operand
    return symbol.isalpha()

def isLeftParenthesis(symbol):
    # checks if symbol is a left parenthesis
    return symbol == '('

def isRightParenthesis(symbol):
    # checks if symbol is a right parenthesis
    return symbol == ')'

def reverseExpression(expression):
    # reverses the expression for the stack operations
    expression = '(' + expression + ')'
    expression = expression[len(expression)::-1]
    return [symbol for symbol in expression]

def hierarchy(symbol):
    # checks the hierarchy of the operands
    switcher = {
        '*': 2,
        '/': 2,
        '+': 1,
        '-': 1
    }

    return switcher.get(symbol)

def leftToRight(stackOperator, newOperator):
    # checks for left to right associativity
    if newOperator == '/' and stackOperator == '*':
        return False
    elif newOperator == '*' and stackOperator == '/':
        return True
    elif newOperator == '-' and stackOperator == '+':
        return True
    elif newOperator == '+' and stackOperator == '-':
        return False

def infixToPostfix(expression):
    # converts the postfix expression to infix expression
    infix = reverseExpression(expression)
    operatorStack = []
    postfix = []

    while len(infix) > 0:
        # iterates through the expression stack and adds to the infix expression stack
        # accordingly
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
            topOperator = operatorStack.pop()

            if not isLeftParenthesis(topOperator):

                if hierarchy(symbol) > hierarchy(topOperator):
                    operatorStack.append(topOperator)
                    operatorStack.append(symbol)

                elif hierarchy(symbol) == hierarchy(topOperator):
                    if leftToRight(topOperator, symbol):
                        postfix.append(topOperator)
                        operatorStack.append(symbol)
                    else:
                        operatorStack.append(topOperator)
                        operatorStack.append(symbol)

                else:
                    postfix.append(topOperator)
                    operatorStack.append(symbol)

            else:
                operatorStack.append(topOperator)
                operatorStack.append(symbol)

    return ''.join(postfix)

def testInfixToPostfix(expression, expected):
    print("Infix expression:", expression)
    print("Expected Infix:", expected)
    print("Postfix result:", infixToPostfix(expression))
    return

if __name__ == "__main__":
    test_expression = "(A+(B*C))-((D/E)*F)"
    test_expected = "ABC*+DE/F*-"
    testInfixToPostfix(test_expression, test_expected)

    print()

    test_expression2 = "A*(B+C*D)+E"
    test_expected2 = "ABCD*+*E+"
    testInfixToPostfix(test_expression2, test_expected2)