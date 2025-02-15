def remove_duplicates(nums):
    unique_nums = []
    for num in nums:
        if num not in unique_nums:
            unique_nums.append(num)
    return unique_nums
user_input = input("Введите числа через пробел: ")

try:
    input_list = list(map(int, user_input.split()))
    output_list = remove_duplicates(input_list)
    print("Список без дубликатов:", output_list)
except ValueError:
    print("Ошибка: пожалуйста, введите только числа через пробел.")