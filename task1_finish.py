#ID посылки 33683452
s = input()
stack = []
for i in s.split(' '):
    try:
        stack.append(int(i))
    except ValueError:
        if i == '-':
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif i == '*':
            a, b = stack.pop(), stack.pop()
            stack.append(b * a)
        elif i == '+':
            a, b = stack.pop(), stack.pop()
            stack.append(b + a)
        elif i == '/':
            a, b = stack.pop(), stack.pop()
            stack.append(b // a)
        else:
            raise NotImplementedError
print(stack[0])
