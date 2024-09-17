import Stack

def infix_to_postfix(infix_expr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    op_stac = Stack.Stack()
    postfix_list = []
    token_list = infix_expr.split()
    
    for token in token_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfix_list.append(token)
        elif token == '(':
            op_stac.push(token)
        
        elif token == ')':
            top_token = op_stac.pop()
        
            while top_token != "(":
                postfix_list.append(top_token)
                top_token = op_stac.pop()
        else:
            while (not op_stac.is_empty()) and (prec[op_stac.peek()] >= prec[token]):
                postfix_list.append(op_stac.pop())
            op_stac.push(token)
    while not op_stac.is_empty():
        postfix_list.append(op_stac.pop())
    return " ". join(postfix_list)

print(infix_to_postfix("A * D + C * G"))