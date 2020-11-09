from functools import reduce

sum1 = reduce(lambda x, y: x + y, [n for n in range(100, 1001)])

print(sum1)