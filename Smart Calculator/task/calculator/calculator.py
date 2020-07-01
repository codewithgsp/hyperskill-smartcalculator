# write your code here
input_string = ''
while input_string != '/exit':
    input_string = input()
    if input_string in ('', '/exit'):
        continue
    print(sum(map(int, input_string.split())))
else:
    print('Bye!')