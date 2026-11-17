from enum import Enum
from datetime import date


class GovernmentType(Enum):
    DEMOCRACY = "Демократія"
    REPUBLIC = "Республіка"
    MONARCHY = "Монархія"
    AUTOCRACY = "Автократія"


class Country:
    def __init__(self, name, capital, code, population, area, gdp, government):
        self.__name = name
        self.__capital = capital
        self.__code = code
        self.__population = population  # осіб
        self.__area = area              # км²
        self.__gdp = gdp                # млрд $
        self.__government = government

    def __del__(self):
        print("Видалено країну:", self.__name)

    # функції доступу
    def get_name(self):
        return self.__name

    def get_population(self):
        return self.__population

    def set_population(self, value):
        self.__population = value

    def get_gdp(self):
        return self.__gdp

    def get_government(self):
        return self.__government

    def density(self):
        return self.__population / self.__area

    def gdp_per_capita(self):
        return self.__gdp * 1e9 / self.__population

    def show(self):
        print(f"{self.__name} ({self.__code}), столиця {self.__capital}, "
              f"населення {self.__population}, площа {self.__area} км², "
              f"ВВП {self.__gdp} млрд $, {self.__government.value}")


class Land:
    def __init__(self, name):
        self.__name = name
        self.__countries = []

    def add_country(self, country):
        self.__countries.append(country)

    def get_countries(self):
        return self.__countries

    def show(self):
        print("\nРегіон:", self.__name)
        for c in self.__countries:
            c.show()


class Film:
    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date


def calculate_population_density(countries):
    for c in countries:
        print(f"Густина {c.get_name()}: {c.density():.1f} осіб/км²")


def print_top_by_gdp(countries, n):
    sorted_list = sorted(countries, key=lambda c: c.get_gdp(), reverse=True)
    print(f"\nТОП-{n} за ВВП:")
    for i in range(n):
        print(f"{i + 1}. {sorted_list[i].get_name()} - {sorted_list[i].get_gdp()} млрд $")


def choose_country(countries, min_population, government):
    """Обирає країну із заданим типом правління та мінімальним населенням,
    яка має найбільший ВВП на душу населення."""
    best = None
    for c in countries:
        if c.get_population() >= min_population and c.get_government() == government:
            if best is None or c.gdp_per_capita() > best.gdp_per_capita():
                best = c
    return best


def main():
    ua = Country("Україна", "Київ", "UA", 38000000, 603550, 180, GovernmentType.REPUBLIC)
    pl = Country("Польща", "Варшава", "PL", 37700000, 312696, 810, GovernmentType.DEMOCRACY)
    de = Country("Німеччина", "Берлін", "DE", 83200000, 357022, 4500, GovernmentType.DEMOCRACY)
    by = Country("Білорусь", "Мінськ", "BY", 9200000, 207600, 72, GovernmentType.AUTOCRACY)

    europe = Land("Європа")
    for c in (ua, pl, de, by):
        europe.add_country(c)
    europe.show()

    calculate_population_density(europe.get_countries())
    print_top_by_gdp(europe.get_countries(), 3)

    best = choose_country(europe.get_countries(), 10000000, GovernmentType.DEMOCRACY)
    print("\nОбрана країна:")
    best.show()

    ua.set_population(37500000)
    print("\nНове населення України:", ua.get_population())

    films = [Film("Фільм C", date(2021, 5, 20)),
             Film("Фільм A", date(2015, 1, 10)),
             Film("Фільм B", date(2018, 9, 3))]
    films.sort(key=lambda f: f.release_date)
    print("\nФільми за датою випуску:")
    for f in films:
        print(f.title, f.release_date)


main()