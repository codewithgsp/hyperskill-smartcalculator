# out = []
# y = 0
# for x in input():
#     y += int(x)
#     out.append(y)
# print(out)
from itertools import accumulate

int_list = [int(i) for i in input()]
print(list(accumulate(int_list)))