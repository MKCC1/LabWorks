numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
# TODO заменить значение пропущенного элемента средним арифметическим
numbers_without_none = numbers[0:4] + numbers[5:]
total = sum(numbers_without_none)
count = (len(numbers))
avg = total / count
numbers[4] = avg
#print(f'Список без пропущенного {numbers_without_none}\nсумма:{total}\nдлинна:{count}\nср.арф.:{avg}')
print("Измененный список:", numbers)
