"=================Абстракция================="
# абстракция - принцип ООП, в котором создается абстрактый класс (класс - пустышка), в котором задаются названия аттрибутов и методов, для этого, чтобы в дочерних кдассах переопределить их нужным образом. от абстрактных классов мы не создаем обьектов, потому что в них есть только навзвания и нет логики

from abc import ABC, abstractclassmethod, abstractproperty

class AbstractAnimal(ABC):
    @abstractclassmethod
    def voice(self):
        pass

    @abstractproperty
    def legs(self):
        pass

# obj = AbstractAnimal() TypeError: Can't instantiate abstract class AbstractAnimal with abstract methods legs, voice

class Dog(AbstractAnimal):
    pass

# obj = Dog() TypeError: Can't instantiate abstract class Dog with abstract methods legs, voice

class Dog(AbstractAnimal):
    legs = 4

    def voice(self):
        print('gav-gav')
    
class Cat(AbstractAnimal):
    legs = 4

    def voice(self):
        print('meow')

dog1 = Dog()
dog1.voice() #gav-gav

cat1 = Cat()
cat1.legs #4