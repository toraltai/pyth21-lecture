class Person:
    arms = 2
    legs = 2

    def __init__(self, name, age):
        """
        функция, которая вызывается, когда мы создаем обьект от класса
        self - ссылка на созданный обьект
        """
        self.name = name # мы добавляем в обьект self новый аттрибут name
        self.age = age # новый аттрибут age

    def add_age(self):
        """
        функция, которая принимает обьект и изменяет его возраст на 1
        """
        self.age += 1

    def __str__(self):
        """
        функция, которая вызывается, когда мы оборачиваем обьект в класс str или когда принтуем обьект
        функция __str__ ничего кроме self не принимает и обязательно должна возвращать строку
        """
        return f"{self.name} - {self.age} y.o"

person1 = Person("Настя", 50)
print(person1)

person2 = Person("Жаркынай", 15)
print(person2)