from collections import deque

stack = deque()
number_of_operations = int(input())
for _ in range(number_of_operations):
    operation = input()
    if operation.startswith('PUSH'):
        stack.append(operation.replace('PUSH', '').strip())
    elif operation.startswith('POP'):
        stack.pop()
for _ in range(len(stack)):
    print(stack.pop())
