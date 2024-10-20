# TODO Найдите количество книг, которое можно разместить на дискете
# Память на книгу в байтах
one_char_in_book = 4
one_string_in_book = 25 * one_char_in_book
one_list_in_book = 50 * one_string_in_book
one_book_in_book = 100 * one_list_in_book #Количество байтов
# Конвертирование
one_book_in_book_kb = one_book_in_book / 1024
one_book_in_book_mb = one_book_in_book_kb / 1024
#print(f'Количество БАЙТ на 1 книгу: {one_book_in_book}\nКоличество килобайт в книге:{one_book_in_book_kb}\nКоличество мегабайт в книге:{one_book_in_book_mb}')
total_books = int(1.44 // one_book_in_book_mb)
print("Количество книг, помещающихся на дискету:", total_books)


# #От обратного
# const_disk = 1.44
# const_disk_in_kb = 1.44 * 1024
# const_disk_in_b = const_disk_in_kb * 1024
# total_books_another = int(const_disk_in_b / one_book_in_book)
# print("Количество книг, помещающихся на дискету:", total_books_another)