from abc import ABC, abstractmethod
from dataclasses import dataclass, field

class Animal(ABC):
    _name : str
    _species: str
    _hungry_status: bool=True

    @abstractmethod
    def make_sound(self) -> str:
        pass
    
    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def species(self) -> str:
        return self._species

    @property
    def hungry_status(self) -> str:
        return 'Голоден' if self._hungry_status == True else 'Не голоден'

    @hungry_status.setter
    def hungry_status(self, hungry_status: bool) -> None:
        self._hungry_status = hungry_status

    def feed(self) -> str:
        return f'{self._name} покормлен' if self._hungry_status == True else f'{self._name} не голоден'

    def __str__(self) -> str:
        return f'{self.name}:\n * Вид - {self.species}\n * Уровень сытости - {self.hungry_status}'


class Lion(Animal):

    def __init__(self, _name: str, _species: str, _hungry_status: bool) -> None:
        super().__init__(_name, _species, _hungry_status)

    def make_sound(self) -> str:
        return 'Lion Grwwwww!'

class Elephant(Animal):

    def __init__(self, _name: str, _species: str, _hungry_status: bool) -> None:
        super().__init__(_name, _species, _hungry_status) 

    def make_sound(self) -> str:
        return 'Elephant\'s Whooooo' 

class Monkey(Animal):

    def __init__(self, _name: str, _species: str, _hungry_status: bool) -> None:
        super().__init__(_name, _species, _hungry_status)

    def make_sound(self):
        return 'Monkey\'s Whu-Whu-A-A'

class Zoo:
    zoo: list[Animal] = field(default_factory=list)

    def add_animal(self, animal: Animal) -> None:
        self.zoo.append(animal)

    def feed_all_animals(self) -> str:
        for animal in self.zoo:
            animal.hungry_status = False
        return 'Все животные покормлены'

    def return_all_sounds(self) -> list[str]:
        return [animal.make_sound() for animal in self.zoo] 

if __name__ == '__main__':
    l = Lion('Лев', 'Лев обыкновенный', False)
    e = Elephant('Слон', 'Серый слон', True)
    print(l.feed())
    print(l)
    print(e)
    print(e.feed())

   # e.hungry_status = True
    print(e.hungry_status)
    print(e)
    print(e.feed())
    print(e.hungry_status)

    print(e.name)

    zoo = Zoo()
    zoo.add_animal(l)
    zoo.add_animal(e)
    print(zoo.return_all_sounds())
    print(l.hungry_status)
    print(zoo.feed_all_animals())
    print(l.hungry_status)
