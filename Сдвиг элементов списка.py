def shift_list(nums, k):
    k = k % len(nums)
    shifted_list = nums[-k:] + nums[:-k]
    return shifted_list
try:
    user_input = input("Введите список чисел через пробел: ")
    k = int(input("Введите количество позиций для сдвига (k): "))
    nums = list(map(int, user_input.split()))
    result = shift_list(nums, k)
    print("Ввод:", nums, ", k =", k)
    print("Вывод:", result)
except ValueError:
    print("Ошибка: пожалуйста, введите корректные данные (числа через пробел и целое число для k).")