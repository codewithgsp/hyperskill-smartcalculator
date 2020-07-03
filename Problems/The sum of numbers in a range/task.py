def range_sum(numbers, start, end):
    _sum = 0
    for number in numbers:
        if start <= number <= end:
            _sum += number
    return _sum


input_numbers = list(map(int, input().split()))
a, b = list(map(int, input().split()))
print(range_sum(input_numbers, a, b))