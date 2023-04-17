nums = input("Введите последовательность чисел через пробел: ").split()
num = int(input("Введите любое число: "))
try:
    numlist = list(map(int, nums))
except ValueError:
    print("Ошибка ввода. Выход из программы.")
    exit()
else:
    pass

for i in range(1, len(numlist)):
    x = numlist[i]
    idx = i
    while idx > 0 and numlist[idx-1] > x:
        numlist[idx] = numlist[idx-1]
        idx -= 1
    numlist[idx] = x
print(numlist)


def binary_search(array, element, left, right):
    if left > right:
        print("Введенное вами число отсутствует в списке.")

    middle = (right + left) // 2
    if array[middle] == element:
        return middle - 1
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)





array = numlist
element = num
print(binary_search(array, element, 0, numlist[-1]))