import random

my_list = []
for i in range(10):
     my_list.append(random.randint(1, 100))

new_list = [my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i - 1]]
print(my_list)
print(new_list)
