class Animal:
    def voice(self):
        pass


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


# Вызываем для каждого переопределенный метод voice()
cat.voice()
dog.voice()
sheep.voice()
