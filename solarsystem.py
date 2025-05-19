from dataclasses import dataclass, field

@dataclass
class Star:
    name: str
    mass: float
    temperature: float 

    def __post_init__(self) -> None:
        if self.mass <= 0: 
            raise ValueError('Звезда должна иметь положительную массу')

    def shine(self) -> str:
       return 'Светит ярко' if self.temperature > 5000 else 'Светит тускло'

    def __str__(self) -> str:
        return f'Название: {self.name}, Масса: {self.mass}, Температура: {self.temperature}'
    

@dataclass
class Planet:
    name: str
    mass: float    
    distance_to_star: float 
    orbital_period: float 
    
    def __post_init__(self) -> None:
        if self.mass <= 0 or self.distance_to_star <= 0: 
            raise ValueError('Звезда должна иметь положительную массу или расстояние')
        
    def orbit(self) -> str:
        return f'{self.name} обращается вокруг звезды за {self.orbital_period} дней на расстонии {self.distance_to_star}'
    
    def position_after_years(self, years: int) -> float:
        return (float(years * 365) % self.orbital_period) / self.orbital_period
    
    def __str__(self) -> str:
        return f'Название: {self.name}, Масса: {self.mass}, Расстояние до звезды: {self.distance_to_star}, Орбитальный период в днях: {self.orbital_period}'

@dataclass
class SolarSystem:
    star: Star
    planets: list[Planet] = field(default_factory=list)

    def add_planet(self, planet: Planet) -> None:
        if any(existing.name == planet.name for existing in self.planets):
            raise ValueError(f"Планета с именем '{planet.name}' уже существует в системе.")
        self.planets.append(planet)
        
    def display_info(self) -> str:
        lines = [
            f"Звезда: {self.star.name}, Масса: {self.star.mass} кг, Температура: {self.star.temperature} К",
            "Планеты:"
        ]
        for planet in self.planets:
            lines.append(
                f"- {planet.name}, Масса: {planet.mass} кг, "
                f"Расстояние до звезды: {planet.distance_to_star} млн км, "
                f"Орбитальный период: {planet.orbital_period} дней"
            )
        return '\n'.join(lines)

    def simulate(self, years: int) -> list[str]:
        results = [f"Симуляция положения планет через {years} лет:"]
        for planet in self.planets:
            position_fraction: float = planet.position_after_years(years)
            degrees: float = round(position_fraction * 360, 2)
            results.append(f"- {planet.name} будет на {degrees}° своей орбиты.")
        return results

if __name__ == "__main__":        
    sun = Star("Солнце", 1.989e30, 5778)
    solar_system = SolarSystem(sun)

    earth = Planet("Земля", 5.972e24, 149.6, 365.25)
    mars = Planet("Марс", 6.39e23, 227.9, 687)
    mercury = Planet("Меркурий", 3.3e23, 57.9, 88)

    solar_system.add_planet(earth)
    solar_system.add_planet(mars)
    solar_system.add_planet(mercury)

    print(solar_system.star.shine())
    print(solar_system.display_info())

    print(earth.orbit())

    for line in solar_system.simulate(3):
        print(line)