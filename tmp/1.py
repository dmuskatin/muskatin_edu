# import os
#
# current_directory = os.getcwd()
# print(f'Этот проект находится в директории {current_directory}' )


# b = int(input())
#
# if a > b:
#     print("Больше")
# elif a == b:
#     print("Равно")
# else:
#     print("Меньше")


# a = input('введите число')
#
# if int(a) > 500:
#     print('Это число больше 500')
# else:
#     print('Это число меньше 500')
#


import json

with open('user_info.json', 'r') as file:
    data = json.load(file)

# Теперь 'data' содержит объекты Python (например, словарь или список)
print(data)
