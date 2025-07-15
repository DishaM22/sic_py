def precedence(op):
    if op in ('+', '-'):
        return 1
    elif op in ('*', '/'):
        return 2
    elif op in ('^', '%'):
        return 3
    return 0

def right_associativity(op):
    return op == '^'

def infix_to_postfix(expr):
    values = []
    stack = []
    expr = expr.replace(" ", "")  # Clean expression

    for i in expr:
        if i.isalnum():  # Operand: letter or digit
            values.append(i)
        elif i == '(':
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                values.append(stack.pop())
            stack.pop()  # remove '('
        else:  # Operator
            while (stack and stack[-1] != '(' and
                   (precedence(stack[-1]) > precedence(i) or
                    (precedence(stack[-1]) == precedence(i) and not right_associativity(i)))):
                values.append(stack.pop())
            stack.append(i)

    while stack:
        values.append(stack.pop())

    return ' '.join(values)

# Run this exactly
expr = "a * (b + c / d) ^ e - f"
postfix = infix_to_postfix(expr)
print("Postfix expr:", postfix)
