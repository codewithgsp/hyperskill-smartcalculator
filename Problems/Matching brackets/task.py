from collections import deque
stack_start = deque()
stack_end = deque()
for i, character in enumerate(input()):
    if character == ')':
        stack_end.append(i)
    if character == '(':
        stack_start.append(i)
if len(stack_start) == len(stack_end):
    i = 0
    while i < len(stack_start):
        if stack_start[i] > stack_end[i]:
            print('ERROR')
            break
        i += 1
    else:
        print('OK')
else:
    print('ERROR')



