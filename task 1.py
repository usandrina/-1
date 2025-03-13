import doctest


    class Brick:
        def __init__(self, kind: str, strength: int):
            """
            Создание и подготовка к работе объекта "Кирпич"

            :param kind: Вид кирпича
            :param strength: Прочность кирпича

            Примеры:
            >>> brick = Brick("облицовочный", 100)  # инициализация экземпляра класса
            """
            if not isinstance(kind, str):
                raise TypeError("Вид кирпича должен быть типа str")
            self.kind = kind
            if not isinstance(strength, int):
                raise TypeError("Прочность кирпича должна быть int")
            if strength < 0:
                raise ValueError("Прочность не может быть отрицательным числом")
            self.strength = strength

        def brick_load(self, load: float) -> None:
            """
            Нагружаем кирпич.
            :param load: Нагрузка на кирпич

            :raise ValueError: Если нагрузка на кирпич превышает прочность кирпича

            Примеры:
            >>> brick = Brick("строительный", 200)
            >>> brick.brick_load(200)
            """
            if not isinstance(load, (int, float)):
                raise TypeError("Нагрузка должна быть типа int или float")
            if load < 0:
                raise ValueError("Нагрузка должна положительным числом")
            ...


        def is_facing_brick(self) -> bool:
            """
            Функция которая проверяет подходит ли кирпич для облицовочных работ

            :return: Подходит ли кирпич для облицовочных работ

            Примеры:
            >>> brick = Brick("строительный", 200)
            >>> brick.is_facing_brick()
            """
            ...


    class Dumbbell
        def __init__(self, bar: float, plate: int,):
            """
            Создание и подготовка к работе объекта "Гантеля"

            :param bar: Вес грифа гантели
            :param plate: Вес блинов гантели

            Примеры:
            >>> dumbbell = Dumbbell(1.5, 2)  # инициализация экземпляра класса
            """
            if not isinstance(bar, (int, float)):
                raise TypeError("Вес грифа должен быть типа float")
            self.bar = bar
            if not isinstance(plate, int):
                raise TypeError("Вес блинов должен быть int")
            if bar < 0 or plate < 0:
                raise ValueError("Вес не может быть отрицательным числом")
            self.plate = plate

        def is_plate_dumbbell(self) -> bool:
            """
            Функция которая проверяет есть ли на грифе блины

            :return: Есть ли на грифе блины

            Примеры:
            >>> dumbbell = Dumbbell(1.5, 0)
            >>> dumbbell.is_plate_dumbbell()
            """
            ...

        def add_plates_to_dumbble(self, weight: int) -> None:
            """
            Добавление блинов на гантелю.
            :param weight: Вес добавляемых блинов

            Примеры:
            >>> dumbbell = Dumbbell(1.5, 2)
            >>> dumbbell.add_plates_to_dumbble(2)
            """
            if not isinstance(weight, int):
                raise TypeError("Добавляемый вес быть типа int")
            if weight < 0:
                raise ValueError("Добавляемый вес должен быть положительным числом")
            ...


    class Person:

        def __init__(self, name: str, age: int):
            """

            :param name: Имя человека
            :param age: Возраст человека

            Примеры:
            >>> person = Person("Kate", 22)
            """
            if not isinstance(name, str):
                raise TypeError("Имя должно быть типа str")
            self.name = name
            if not isinstance(age, int):
                raise TypeError("Возраст должен быть int")
            if age < 0:
                raise ValueError("Возраст не может быть отрицательным числом")
            self.age = age

        def display_info(self):
            print(f"Name: {self.name}  Age: {self.age}")
            """
            Вывод на дисплей информации о человеке.
        
            Примеры:
            tom = Person("Tom", 23)
            tom.display_info() 
            """


        def is_adult_person(self) -> bool:
            """
            Функция которая проверяет совершеннолетний ли человек

            :return: Совершеннолетний ли человек

            Примеры:
            >>> Ann = Person("Ann", 20)
            >>> brick.is_adult_person()
            """
            ...

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации