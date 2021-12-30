#괄호의 값 [Silver 2]

import sys

bracket = str(sys.stdin.readline().strip())

bracket = list(bracket)

stack = []

while(len(bracket)>0):
    a = bracket.pop(0)

    if(a == '(' or a =='['):
        stack.append(a)
#    print(stack)

    if(a == ')'):
        _sum = 0
        while(True):
            if not stack:
                print(0)
                sys.exit(0)
            k = stack.pop()
            if(k=='('):
                break
            if (str(type(k)) != "<class 'int'>"):
                print(0)
                sys.exit(0)
            if(str(type(k)) == "<class 'int'>"):
                _sum = _sum + k
        if(_sum == 0):
            stack.append(2)
        elif(_sum != 0):
            stack.append(_sum*2)

    elif (a == ']'):
        _sum = 0
        while(True):
            if not stack:
                print(0)
                sys.exit(0)
            k = stack.pop()
            if(k=='['):
                break
            if (str(type(k)) != "<class 'int'>"):
                print(0)
                sys.exit(0)
            if(str(type(k)) == "<class 'int'>"):
                _sum = _sum + k
        if (_sum == 0):
            stack.append(3)
        elif (_sum != 0):
            stack.append(_sum * 3)

sum_all = 0
while stack:
    n = stack.pop()
    if(str(type(n)) != "<class 'int'>"):
        print(0)
        sys.exit(0)
    sum_all = sum_all+n

print(sum_all)