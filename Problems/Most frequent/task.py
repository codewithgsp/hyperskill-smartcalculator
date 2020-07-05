from collections import Counter
text = ("all I want is a proper cup of coffee made in a proper copper coffee pot. "
        "I may be off my dot but I want a cup of coffee from a proper coffee pot.")
n = int(input())

freq_list = Counter(text.split(' '))
for list_ in freq_list.most_common(n):
        print(list_[0], list_[1])
