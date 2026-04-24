import re

def validate_city(city: str) -> str:
    if not isinstance(city, str):
        raise TypeError("Тип города должен быть строкой")
    city = city.strip()
    pattern = r"^[A-Za-z\s-]+$"
    if not re.match(pattern, city):
        raise ValueError("Неправильное название города")
    return city


def find_country(countries, city_n: str):
    city_n = city_n.strip().lower()
    for country in countries:
        for city in country.cities:
            if city.lower() == city_n:
                return country.name
    return None

def get_all_cities(countries):
    cities = []
    for country in countries:
        cities.extend(country.cities)
    return cities

