# the object_list has already been defined
# write your code here

from collections.abc import Hashable
count = 1
object_dict = {}
#  object_list = [1, 397, 27468, -95, 1309, 397, -539874, -240767, -95, 397]
for _obj in object_list:
    if isinstance(_obj, Hashable):
        object_dict[_obj] = object_dict.get(_obj, 0) + count
sum_ = 0
for _obj in object_dict:
    if object_dict[_obj] > 1:
        sum_ += object_dict[_obj]
print(sum_)
