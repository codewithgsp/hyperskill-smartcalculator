from collections import deque

student_queue = deque()
passed_queue = deque()
number_of_records = int(input())

for _ in range(number_of_records):
    student = input()
    if student.startswith('READY'):
        student_queue.appendleft(student.replace('READY', '').strip())
    elif student.startswith('EXTRA'):
        student_queue.appendleft(student_queue.pop())
    elif student.startswith('PASSED'):
        passed_queue.appendleft(student_queue.pop())
for _ in range(len(passed_queue)):
    print(passed_queue.pop())
