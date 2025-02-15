def merge_unique_lists(list1, list2):
    unique_nums = []
    combined_list = list1 + list2
    for num in combined_list:
        if num not in unique_nums:
            unique_nums.append(num)
    return unique_nums
try:
    user_input1 = input("Введите первый список чисел через пробел: ")
    user_input2 = input("Введите второй список чисел через пробел: ")
    list1 = list(map(int, user_input1.split()))
    list2 = list(map(int, user_input2.split()))
    result = merge_unique_lists(list1, list2)
    print("Ввод:", list1, ",", list2)
    print("Вывод:", result)
except ValueError:
    print("Ошибка: пожалуйста, введите только числа через пробел.")