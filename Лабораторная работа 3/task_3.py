# TODO  Напишите функцию count_letters
def count_letters(str_):
    dict_chars = {}
    str_ = str_.lower()
    for char in str_:
        if char.isalpha():
            if char in dict_chars:
                dict_chars[char] += 1
            else:
                dict_chars[char] = 1
    return dict_chars


# TODO Напишите функцию calculate_frequency
def calculate_frequency(letter_counts):
    res = {}
    count_letters = sum(letter_counts.values())
    for key_, value_ in letter_counts.items():
        res[key_] = value_
        print(f"{key_}: {(value_ / count_letters):.2f}")
    return res


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте

init_first_def = count_letters(main_str)
init_second_def = calculate_frequency(init_first_def)
# print(init_second_def)
