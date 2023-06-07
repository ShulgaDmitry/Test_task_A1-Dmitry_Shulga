#Необходимо создать класс Animal, который имеет атрибуты Name (тип животного),
# Color (его расцветку) и Voice (издаваемый звук). Написать функцию, которая возвращает строку вида
# «It says <Voice>.», где <Voice> является уникальным атрибутом класса Animal. Задать три экземпляра класса Cow,
# Cat, Dog с уникальными атрибутами для каждого. Для каждого экземпляра вывести строку вида «<Name> is <Color>.
# It says <Voice>.»

class Animal:

    def __init__(self, name, color, voice):
        self.name = name
        self.color = color
        self.voice = voice

    def special_command(self):
        print(f"{self.name} is {self.color}")

    def special_sound(self):
        print(f"It says {self.voice}")


cow = Animal("Mammal", "ginger", "Mu")
cow.special_command()
cow.special_sound()
cat = Animal("Mammal", "black", "Meow")
cat.special_command()
cat.special_sound()
dog = Animal("Mammal", "white", "Woof")
dog.special_command()
dog.special_sound()
