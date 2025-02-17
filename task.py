from typing import List


class Animal:
    """
    Базовый класс для животных

    Атрибуты:
        name (str): Имя животного
        species (str): Тип животного
        age (int): Возраст животного
        sound (bool): Может ли подовать звуковые сигналы

    Методы:
        __init__(name, species, age): Инициализация класса
        __str__(): Возвращает строковое представление объекта
        __repr__(): Возвращает строку для отладки
        make_sound(): Издает звук
    """

    def __init__(self, name: str, species: str, age: int, sound: bool):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound

    def __str__(self) -> str:
        if 10 < self.age % 100 < 20:
            age_str = "лет"
        elif self.age % 10 == 1:
            age_str = "год"
        elif 2 <= self.age % 10 <= 4:
            age_str = "года"
        else:
            age_str = "лет"
        return f"Имя {self.name} - тип {self.species}, возраст {self.age} {age_str}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} name={self.name!r} species={self.species!r} age={self.age!r}, sound={self.sound!r}"

    def make_sound(self) -> str:
        return "Может издавать звуки" if self.sound else "Не может издавать звуки"


class Cat(Animal):
    """
    Класс, представляющий кошку

    Атрибуты:
        name (str): Имя кошки
        species (str): Тип животного, всегда "Кошка"
        age (int): Возраст кошки
        poroda (str): Порода кошки

    Методы:
        __init__(name, age, poroda): Инициализация класса
        __str__(): Перегрузка метода для строкового представления
        __repr__(): Перегрузка метода для отладки
        make_sound(): Перегрузка метода для звука кошки
    """

    def __init__(self, name: str, age: int, sound: bool, poroda: str):
        super().__init__(name, "Кошка", age, sound)
        self.poroda = poroda

    def __str__(self) -> str:
        return f"{super().__str__()}, порода {self.poroda}"

    def __repr__(self) -> str:
        return f"{super().__repr__()}, poroda={self.poroda}"

    def make_sound(self) -> str:
        """Перегрузка метода для звука кошки"""
        return "Кошка говорит Мяу!" if self.sound else super().make_sound()


class Dog(Animal):
    """
    Класс, представляющий собаку.

    Атрибуты:
        name (str): Имя собаки.
        species (str): Тип животного, всегда "Собака".
        age (int): Возраст собаки.
        poroda (str): Порода собаки.

    Методы:
        __init__(name, age, poroda): Инициализация класса.
        __str__(): Перегрузка метода для строкового представления.
        __repr__(): Перегрузка метода для отладки.
        make_sound(): Перегрузка метода для звука собаки.
    """

    def __init__(self, name: str, age: int, sound: bool, poroda: str):
        super().__init__(name, "Собака", age, sound)
        self.poroda = poroda

    def __str__(self) -> str:
        return f"{super().__str__()}, порода {self.poroda}"

    def __repr__(self) -> str:
        return f"{super().__repr__()}, poroda={self.poroda})"

    def make_sound(self) -> str:
        """Перегрузка метода для звука собаки"""
        return "Собака говорит - Гав!" if self.sound else super().make_sound()


if __name__ == '__main__':
    snake = Animal(name="Ползуха", age=12, sound=False, species="Змея")
    cat = Cat(name="Барсик", age=3, sound=True, poroda="Сиамская")
    mutecat = Cat(name="Барсик", age=3, sound=False, poroda="Сиамская")
    dog = Dog(name="Шарик", age=5, sound=True, poroda="Лабрадор")

    print(snake.__repr__())
    print(cat.__repr__())

    print(snake)
    print(cat)
    print(mutecat)
    print(dog)

    print(snake.make_sound())
    print(cat.make_sound())
    print(mutecat.make_sound())
    print(dog.make_sound())
