opening_brackets=["(","{","["]
closing_brackets=[")","}","]"]
def check(mystr):
    stack = []
    for i in mystr:
        if i in opening_brackets:
          stack.append(i) 
        elif i in closing_brackets:
            pos = closing_brackets.index(i)
            if len(stack) > 0 and opening_brackets[pos] == stack[len(stack)-1]:
               stack.pop()
    if stack == []:
       print("the string is balanced")
    else:
       print("the string is not balanced")
y = input("Make an expression(string)")
check(y)
 