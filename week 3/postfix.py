def precedence(op):
    if op=='+' or op=='-' :
        return 1
    if op=='*' or op=='/':
        return 2
    if op=='^' or op=='% ':
        return 3
    return 0

def apply_op(a,b,op):
    if op=='+':
        return a+b
    if op=='-':
        return a-b
    if op=='*':
        return a*b
    if op=='/':
        return a//b
    if op=='^':
        return a**b
    if op=='%':
        return a%b

def postfix_evaluation(expr):
    stack=[]
    expr=expr.split()
    for i in expr:
        if i.isdigit():
            stack.append(int(i))
        else:
            a=stack.pop()
            b=stack.pop()
            result=apply_op(a,b,i)
            stack.append(result)
    return stack[-1]

expr="4 5 6 + *"
print("Result:",postfix_evaluation(expr))