class Animal:
    num_of_insts = 0

    def __init__(self):
        Animal.num_of_insts += 1

    def voice(self):
        pass

    @staticmethod
    def count_instances():
        print(Animal.num_of_insts)


class Cat(Animal):
    def voice(self):
        print("Мяу")


class Dog(Animal):
    def voice(self):
        print("Гав")


class Sheep(Animal):
    def voice(self):
        print("Ббееее")


# Создаем по одному экземпляру всех наследников
cat = Cat()
dog = Dog()
sheep = Sheep()

# Вызываем статический метод для вывода количества экземпляров
Animal.count_instances()
