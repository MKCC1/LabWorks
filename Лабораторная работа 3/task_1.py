class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """Класс бумажной книги"""

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Кол-во страниц целлочисленное значение")
        if value <= 0:
            raise ValueError("В книге больше 0 страниц")
        self._pages = value

    def __str__(self):
        str_ = super().__str__()
        return f"{str_}. Страниц: {self.pages}"


class AudioBook(Book):
    """Класс аудио книги"""

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, value: float):
        if not isinstance(value, (int, float)):
            raise TypeError("Время положительное число")
        if value <= 0:
            raise ValueError("Время больше 0")
        self._duration = float(value)

    def __str__(self):
        str_ = super().__str__()
        return f"{str_}. Длительность: {self.duration}"
    
if __name__ == '__main__':
    book = Book("Старик и море", "Эрнест Хемингуэй")
    paperbook = PaperBook("Солярис", "Станислав Лем", 480)
    audiobook = AudioBook("Цвет из иных миров", "Говард Лавкрафт", 20.5)
    
    print(book)
    print(paperbook)
    print(audiobook)

    print(repr(book))
    print(repr(paperbook))
    print(repr(audiobook))
    
    try:
        book.name = "Новое название"
    except AttributeError as e:
        print(e)

    try:
        paperbook.pages = -10
    except ValueError as e:
        print(e)

    try:
        audiobook.duration = "двадцать"
    except TypeError as e:
        print(e)
