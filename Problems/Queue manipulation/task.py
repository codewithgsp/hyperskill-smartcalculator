from collections import deque

queue = deque()
number_of_action = int(input())
for _ in range(number_of_action):
    action = input()
    if action.startswith('ENQUEUE'):
        queue.appendleft(action.replace('ENQUEUE', '').strip())
    elif action.startswith('DEQUEUE'):
        queue.pop()
for _ in range(len(queue)):
    print(queue.pop())
