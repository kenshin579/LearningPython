# This is not a valid Python module - Don't run it.

>> > test = [2, 5, 8, 0, 0, 1, 0]
>> > list(filter(None, test))  # note: 함수가 None이면 identity 함수로 가정하고 요소가 false인 거는 제거됨
[2, 5, 8, 1]
>> > list(filter(lambda x: x, test))  # equivalent to previous one
[2, 5, 8, 1]
>> > list(filter(lambda x: x > 4, test))  # keep only items > 4
[5, 8]
