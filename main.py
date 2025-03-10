# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`)
# и методы (`make_sound()`, `eat()`) для всех животных.

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f'{self.name} издает звук')

    def eat(self):
        print(f'{self.name} ест')

# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`.
# Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для `make_sound()`).

class Bird(Animal):
    def make_sound(self):
        print(f'{self.name} щебечет')

class Mammal(Animal):
    def make_sound(self):
        print(f'{self.name} общается')

class Reptile(Animal):
    def make_sound(self):
        print(f'{self.name} шипит')

# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает список животных и
# вызывает метод `make_sound()` для каждого животного.

animals = [Bird("Чижик",2), Mammal("Корова",5), Reptile("Уж",3)]

for animal in animals:
    animal.make_sound()

# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках.
# Должны быть методы для добавления животных и сотрудников в зоопарк.

class Zoo:
    def __init__(self):
        self.animals = [Animal("Тигр", 5)]
        self.staff = [ZooKeeper("Петя"), Veterinarian("Вася")]

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f'{animal.name} добавлен в зоопарк')

    def add_staff(self, staff):
        self.staff.append(staff)
        print(f'{staff.name} добавлен в персонал зоопарка')

    def show_staff(self):
        print("Список сотрудников зоопарка:")
        for staff_member in self.staff:
            print(f'- {staff_member.name}')

    def show_animals(self):
        print("Список животных зоопарка:")
        for animal in self.animals:
            print(f'- {animal.name}')

# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические методы
# (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).

# Классы сотрудников
class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f'{self.name} кормит {animal.name}')

class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f'{self.name} лечит {animal.name}')


# Создаю и добавляю объекты

zoo = Zoo()
animal1 = Bird("Попугай", 1)
animal2 = Mammal("Лев", 4)

staff1 = ZooKeeper("Ваня")
staff2 = Veterinarian("Аня")

zoo.add_animal(animal1)
zoo.add_animal(animal2)
for animal in animals:
    zoo.add_animal(animal)

zoo.add_staff(staff1)
zoo.add_staff(staff2)

zoo.show_staff()
zoo.show_animals()

# Взаимодействия сотрудников с животными

zoo.staff[0].feed_animal(zoo.animals[0])
zoo.staff[1].heal_animal(zoo.animals[3])