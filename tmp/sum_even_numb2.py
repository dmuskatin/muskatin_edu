def sum_even(input_nums):
    even_sum = 0
    for num in input_nums:
        # Проверяем, является ли число четным, с помощью оператора остатка от деления (%)
        if num % 2 == 0:
            even_sum += num
    return even_sum

# Пример использования
numbers = [1, 12, 35, 45, 58, 6, 7, 8, 9, 10]
result = sum_even(numbers)
print(f"Сумма четных чисел в списке {numbers} равна: {result}")