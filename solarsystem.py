from dataclasses import dataclass

@dataclass
class Star:
    name: str
    mass: float
    temperature: float 

    def __post_init__(self):
        if self.mass < 0: 
            raise ValueError('Звезда не может иметь отрицательную массу')

    def shine(self) -> str:
       return 'Светит ярко' if self.temperature > 5000 else 'Светит тускло'

    def __str__(self):
        return f'Название: {self.name}, Масса: {self.mass}, Температура: {self.temperature}'
    

@dataclass
class Planet:
    name: str
    mass: float    
    distance_to_star: float 
    orbital_period: float 
    
    def orbit(self) -> str:
        return f'{self.name} обращается вокруг звезды за {self.orbital_period} дней на расстонии {self.distance_to_star}'

@dataclass
class SolarSystem:
    star: Star
    planets: list[Planet]

    def add_planet(self, planet: Planet) -> None:
        self.planets.append(planet)
        return f'Планета {planet.name} добавлена'

    def display_info(self):
       pass 

sun = Star("Солнце", 1.989e30, 5778)
alpha = Star("Альфа Центавра", -12, -404504)
earth = Planet("Земля", 5.972e24, 149.6e6, 365.25)
mars = Planet("Марс", 6.39e23, 227.9e6, 687)

print(sun)
print(sun.shine())
