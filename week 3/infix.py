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
        return a/b
    if op=='^':
        return a**b
    if op=='%':
        return a%b
    
def evaluate(expr):  
    values=[]
    opr=[]
    i=0

    while i<len(expr):
        if expr[i]==' ':
            i+=1
            continue
        elif expr[i].isdigit():
            val=0
            while i<len(expr) and expr[i].isdigit():
                val=(val*10 )+int(expr [i])
                i+=1
            values.append(val)
            i-=1
        elif expr[i]=='(':
            opr.append(expr[i])

        elif expr[i]==')':
            while opr:
                top = opr[-1]
                if top=='(':
                    opr.pop()
                    break
                else:
                    val2=values.pop()
                    val1=values.pop()
                    op=opr.pop()
                    values.append(apply_op(val1,val2,op))
                
        else:
            while opr and precedence(opr[-1])>=precedence(expr[i]):
                op=opr.pop()
                val2=values.pop()
                val1=values.pop()
                values.append(apply_op(val1,val2,op))
            opr.append(expr[i])
        i+=1

    while opr:
        op=opr.pop()
        val2=values.pop()
        val1=values.pop()
        values.append(apply_op(val1,val2,op))
    return values[-1]
expr="4+5*8-3"
print("Result:",evaluate(expr))



                  
                




    