def precedence(op):
    if op=='+' or op=='-' :
        return 1
    if op=='*' or op=='/':
        return 2
    if op=='^' or op=='% ':
        return 3
    return 0
def right_associativity(op):
    return True
def  infix_to_postfix(expr):
    values=[]
    stack=[]
    i=0

    for i in expr:
        if i.isdigit():
            values.append(i)
        elif i=="(":
            stack.append(i)
        elif i==")":
            while stack and stack[-1]!="(" :
                values.append(stack.pop())
            stack.pop()
        else:
            while (stack and stack[-1]!="(" and (precedence(stack[-1])>precedence(i)) or (precedence(stack[-1]))==precedence(i) and not right_associative(i)):
                values.append(stack.pop())
            stack.append(i)
    while stack:
        values.append(stack.pop())
        return ''.join(output)

expr="4*2*(3^2*5-4)%2"
print("postfix expr:" ,infix_to_postfix(expr))


        


   


            