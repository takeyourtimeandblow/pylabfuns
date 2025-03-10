my_list = list(map(int, input().split(' ')))

# 1
my_list_first = [i for i in my_list if i < 5]
print(my_list_first)

# 2
my_list_second = [i/2 for i in my_list]
print(my_list_second)

# 3
my_list_third = [i*2 for i in my_list if i > 17]
print(my_list_third)

# 4
client_range = int(input())
my_list_fourth = set([i**2 for i in my_list if i <= client_range])
print(my_list_fourth)

# 5
print([i**2 for i in list(map(int, input().split(' ')))])

# 6
print([i**2 for i in list(map(int, input().split(' '))) if i % 2 != 0 and i % 10 != 9])
