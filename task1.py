from datetime import datetime
import doctest


# TODO Написать 3 класса с документацией и аннотацией типов
class Student:
    def __init__(self, full_name: str, level_educate: str, age: int):
        """
        Создание и подготовка к работе объекта "Студент"

        :param full_name: Полное имя студента
        :param level_educate: Урвоень образования
        :param age: Возраст студента
        Примеры:
        >>> student = Student("Максим", "Бакалавриат", 21)  # инициализация экземпляра класса
        """
        if not isinstance(full_name, str):
            raise TypeError("Имя студента должно быть тип str")
        self.full_name = full_name

        if not isinstance(level_educate, str):
            raise TypeError("Уровень образования студенда должна быть типа str")
        self.level_educate = None
        self.check_level_educate(level_educate)

        if not isinstance(age, int):
            raise TypeError("Возраст студента должен быть типа int")
        if age < 16:
            raise TypeError("Возраст студента дожен быть положительным числом, и больше 15 лет ")
        self.age = age

    def check_level_educate(self, level_educate: str) -> str:
        """
        Функция которая проверяет правильно ли введено образование
        """
        level_educate_low = level_educate.lower()
        if level_educate_low in {'бакалавриат', 'специалитет', 'магистратура'}:
            return True
        else:
            raise TypeError("Уровень образования может быть: Бакалавриат, Специалитет, Магистратура")
   
    def birth_year(self, age: int) -> int:
        """
        Функция которая возвращает год дня рождения
        Примеры:
        >>> student = Student("Максим", "Бакалавриат", 21)
        >>> birth_year_result = student.birth_year(student.age)
        >>> 1900 < birth_year_result < datetime.now().year
        True
        """
        return datetime.now().year - age 

class Rectangle:
    def __init__(self, length: float, width: float):
        """
        Создание и подготовка к работе объекта "Фигура"

        :param length: Длина
        :param width: Ширина

        Примеры:
        >>> rectangle = Rectangle(5.2, 12)  # инициализация экземпляра класса
        """
        if not isinstance(length, (int, float)):
            raise TypeError("Длина фигуры должна быть типа int или float")
        if length <= 0:
            raise ValueError("Длина фигуры не может быть отрицательной и должна быть больше 0")
        self.length = length

        if not isinstance(width, (int, float)):
            raise TypeError("Ширина фигуры должна быть типа int или float")
        if width <= 0:
            raise ValueError("Ширина фигуры не может быть отрицательной и должна быть больше 0")
        self.width = width

    def check_figure_on_square(self) -> bool:
        """
        Функция которая проверяет является ли фигура квадратом

        :return: Является ли фигура квадратом

        Примеры:
        >>> rectangle = Rectangle(1.5, 12)
        >>> rectangle.check_figure_on_square()
        False
        >>> rectangle = Rectangle(3, 3)
        >>> rectangle.check_figure_on_square()
        True
        """
        return self.length == self.width
    
    def add_size(self, new_lenght: float = 0, new_widt: float = 0) -> int:
        """
        Функция которая добавляет длину и ширину для фигуры

        :return: Новая длина и/или ширина
        Примеры:
        >>> rectangle = Rectangle(1.5, 12)
        >>> rectangle.add_size(11,1)
        (12.5, 23)
        >>> rectangle = Rectangle(3, 3)
        >>> rectangle.add_size()
        'Вы не задали новых значений'
        """
        if (new_lenght and new_widt) is (None or 0):
            return ("Вы не задали новых значений")
        else:
            self.length = self.length + new_lenght
            self.width = self.width + new_lenght
            return self.length, self.width
        
    def area_figure(self):
        """
        Функция которая считает площадь фигуры

        :return: Площаль фигуры (длина * ширина)

        Примеры:
        >>> rectangle = Rectangle(5, 5)
        >>> rectangle.area_figure()
        25
        >>> rectangle = Rectangle(1, 5)
        >>> rectangle.area_figure()
        5
        """
        return self.width * self.length
    
    def perimeter_figure(self):
        """
        Функция которая считает периметр фигуры

        :return: Площаль фигуры ((длина + ширина) * 2)

        Примеры:
        >>> rectangle = Rectangle(5, 5)
        >>> rectangle.perimeter_figure()
        20
        >>> rectangle = Rectangle(1, 5)
        >>> rectangle.perimeter_figure()
        12
        """
        return (self.width + self.length) * 2
    
class Product:
    def __init__(self, name_prod: str, cost: float, count: int):
        """
        Создание и подготовка к работе объекта "Продукт"

        :param name_prod: Номер карты
        :param cost: Количество баллов
        :param count: Количесвто
        
        Примеры:
        >>> product = Product("Сметана", 100, 2)  # инициализация экземпляра класса
        """
        if not isinstance(name_prod, str):
            raise TypeError("Наименование продукта должно быть типа str")
        self.name_prod = name_prod

        if not isinstance(cost, int):
            raise TypeError("Стоимость продукта должна быть типа int")     
        if cost < 0:
            raise ValueError("Цена продукта должна быть типа положительным")
        self.cost = cost

        if not isinstance(count, int):
            raise TypeError("Количесвто продукта должна быть типа int")
        if count < 0:
            raise ValueError("Количесвто продукта должно быть типа положительным")
        self.count = count

    def change_cost(self, new_cost: float) -> None:
        """
        Функция изменят цену продукта
        >>> product = Product("Сметана", 100, 2)
        >>> product.change_cost(123)
        >>> product.info()
        'Продукт: Сметана, Цена: 123.00р, Кол-во:2'
        """
        if new_cost < 0:
            raise ValueError("Новая цена не может быть отрицательной")
        self.cost = new_cost
    
    def info(self) -> str:
        """
        Функция пичатает информацию о продукте
        :return: информация об объекте класса
        Пример:
        >>> product = Product("Машинка", 100, 2)
        >>> product.info()
        'Продукт: Машинка, Цена: 100.00р, Кол-во:2'
        """
        return f"Продукт: {self.name_prod}, Цена: {self.cost:.2f}р, Кол-во:{self.count}"
    
if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()