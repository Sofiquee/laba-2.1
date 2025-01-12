from abc import ABC, abstractmethod

class Computer(ABC):
    def __init__(self, brand: str, processor: str, ram: int):
        """
        Создание объекта компьютера.

        :param brand: Бренд компьютера
        :param processor: Модель процессора
        :param ram: Объем оперативной памяти в ГБ

        Примеры:
        >>> computer = Computer("Dell", "Intel i7", 16)  # инициализация компьютера
        """
        if not isinstance(brand, str):
            raise TypeError("Бренд должен быть строкой")
        if not isinstance(processor, str):
            raise TypeError("Процессор должен быть строкой")
        if not isinstance(ram, int) or ram <= 0:
            raise ValueError("Объем оперативной памяти должен быть положительным числом")

        self.brand = brand
        self.processor = processor
        self.ram = ram

    @abstractmethod
    def power_on(self) -> None:
        """
        Включение компьютера.

        :return: None

        Примеры:
        >>> computer = Computer("Dell", "Intel i7", 16)
        >>> computer.power_on()
        """
        ...

    @abstractmethod
    def power_off(self) -> None:
        """
        Выключение компьютера.

        :return: None

        Примеры:
        >>> computer = Computer("Dell", "Intel i7", 16)
        >>> computer.power_off()
        """

        class Dog(ABC):
            def __init__(self, name: str, breed: str, age: int):
                """
                Создание объекта собаки.

                :param name: Имя собаки
                :param breed: Порода собаки
                :param age: Возраст собаки в годах

                Примеры:
                >>> dog = Dog("Бобик", "Лабрадор", 5)  # инициализация собаки
                """
                if not isinstance(name, str):
                    raise TypeError("Имя должно быть строкой")
                if not isinstance(breed, str):
                    raise TypeError("Порода должна быть строкой")
                if not isinstance(age, int) or age < 0:
                    raise ValueError("Возраст должен быть положительным числом или нулем")

                self.name = name
                self.breed = breed
                self.age = age

            @abstractmethod
            def bark(self) -> str:
                """
                Лай собаки.

                :return: Звук, который издает собака

                Примеры:
                >>> dog = Dog("Бобик", "Лабрадор", 5)
                >>> dog.bark()  # "Гав!"
                """
                ...

            @abstractmethod
            def fetch(self, item: str) -> None:
                """
                Приносить предмет.

                :param item: Название предмета для принесения
                :return: None

                Примеры:
                >>> dog = Dog("Бобик", "Лабрадор", 5)
                >>> dog.fetch("мяч")
                """

                class Music(ABC):
                    def __init__(self, title: str, artist: str, duration: float):
                        """
                        Создание объекта музыкального произведения.

                        :param title: Название произведения
                        :param artist: Исполнитель произведения
                        :param duration: Продолжительность в минутах

                        Примеры:
                        >>> music = Music("Shape of You", "Ed Sheeran", 4.24)  # инициализация музыки
                        """
                        if not isinstance(title, str):
                            raise TypeError("Название должно быть строкой")
                        if not isinstance(artist, str):
                            raise TypeError("Исполнитель должен быть строкой")
                        if not isinstance(duration, (int, float)) or duration <= 0:
                            raise ValueError("Продолжительность должна быть положительным числом")

                        self.title = title
                        self.artist = artist
                        self.duration = duration

                    @abstractmethod
                    def play(self) -> None:
                        """
                        Воспроизведение музыкального произведения.

                        :return: None

                        Примеры:
                        >>> music = Music("Shape of You", "Ed Sheeran", 4.24)
                        >>> music.play()
                        """
                        ...

                    @abstractmethod
                    def stop(self) -> None:
                        """
                        Остановка воспроизведения музыкального произведения.

                        :return: None

                        Примеры:
                        >>> music = Music("Shape of You", "Ed Sheeran", 4.24)
                        >>> music.stop()
                               """