from collections import deque

stack = deque()
read_books = deque()
number_of_actions = int(input())
for i in range(number_of_actions):
    action = input()
    if action.startswith('BUY'):
        stack.append(action.replace('BUY', '').strip())
    elif action.startswith('READ'):
        read_books.append(stack.pop())
for book in read_books:
    print(book)
