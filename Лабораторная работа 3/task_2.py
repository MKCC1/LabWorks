# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first_group, participants_second_group, split_char = ','):
    return list(set(participants_second_group.split(split_char)).intersection(participants_first_group.split(split_char)))


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, split_char = "."))