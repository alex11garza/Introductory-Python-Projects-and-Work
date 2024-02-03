#Codelab 6 Group 13
#Austin Palmer, Alex Garza, Mariah Lucio, Carrington Turner
class Animal:

  def __init__(self, color, height):
    self.color = color
    self.height = height

  def __str__(self):
    return f"The {self.color} animal is inches tall {self.height}."


class Dog(Animal):

  def bark(self):
    print(f"The {self.color} Bird is barking loudly")

  def __str__(self):
    return super().__str__() + ' (Dog)'


class Bird(Animal):

  def fly(self):
    print(f"The {self.color} Bird is flying through the sky at lighting speed")

  def __str__(self):
    return super().__str__() + ' (Bird)'


class Cat(Animal):

  def meow(self):
    print(f"The {self.color} cat is meowing")

  def __str__(self):
    return super().__str__() + ' (Cat)'


class Horse(Animal):

  def neigh(self):
    print(f"The {self.color} horse is neighing.")

  def __str__(self):
    return super().__str__() + ' (Horse)'


class Frog(Animal):

  def hopping(self):
    print(
      f"The {self.color} frog is hopping along the creek looking for a meal")

  def __str__(self):
    return super().__str__() + ' (Frog)'


class Fish(Animal):

  def swimming(self):
    print(f"The {self.color} fish is swimming in the river")

  def __str__(self):
    return super().__str__() + ' (Fish)'


def main():
  eagle = Bird("Blue", 8)
  eagle.fly()
  print(eagle)

  pup = Dog("spotted", 8)
  pup.bark()
  print(pup)

  horse = Horse("brown", 60)
  horse.neigh()
  print(horse)

  kitty = Cat("orange", 13)
  kitty.meow()
  print(kitty)

  frog = Frog("Green", 2)
  frog.hopping()
  print(frog)

  fish = Fish("Red", 4)
  fish.swimming()
  print(fish)


if __name__ == '__main__':
  main()
