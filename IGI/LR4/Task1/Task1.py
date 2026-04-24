from country import Country
from function import validate_city, find_country
from ArbeitMitCSVundPickle import save_to_csv, save_to_pickle, load_from_csv, load_from_pickle


def data_create():
    CountriesMitCitiesData = {"Deutschland": ["Köln", "Düsseldorf", "Padeborn", "Lippstadt", "Geseke", "Dortmund","Gütersloh"], 
                        "Belarus": ["Borisow", "Braslaw", "Minsk", "Brest", "Neswisch", "Mogilew", "Zhodino"],
                        "Spanien": ["Alicante", "Madrid"],
                        "Mauritius": ["Port-Lui", "Flic En Flac", "Soulliac"],
                        "Montenegro": ["Budva Li", "Kotor", "Podgorica"],
                        "Griechenland": ["Chania", "Platanias", "Rethymnon", "Matala"],
                        "Türkei": ["Istambul", "Antalya"],
                        "Bulgarien": ["Albena", "Varna"],
                        "Ägypten": ["Hurghada"],
                        "Russland": ["Moskow"],
                        "Ukraine": ["Odessa"],
                        "Niederlande": ["Amsterdam"],
                        "Litauen": ["Vilnius"]}
    return [Country(name, cities) for name, cities in CountriesMitCitiesData.items()]
def auswahl_format():
    print("Выберите формат загрузки: ", "1 - CSV,", "2 - pickle")
    while(True):
        auswahl = input("Номер формата: ")
        if auswahl == "1":
            return "csv"
        elif auswahl == "2":
            return "pickle"
        else:
            print("Неверный ввод")

def main():
    countries = data_create()
    save_to_csv(countries, "countries_mit_cities.csv")
    save_to_pickle(countries,"countries_mit_cities.pkl")
    file_format = auswahl_format()
    try:
        if file_format == "csv":
            countries = load_from_csv("countries_mit_cities.csv")
        else:
            countries = load_from_pickle("countries_mit_cities.pkl")
    except FileNotFoundError:
        print("Файл не найден")

    while True:
        print("Список стран и городов сформирован относительно путешествий инстаграмм акаунта jaroslavvchik")
        print("1 - Найти страну по городу")
        print("0 - Выйти")
        auswahl = input("Номер выбора: ")
        if auswahl == "1":
            city = input("Ведите город: ")
            city = validate_city(city)
            result = find_country(countries, city)
            if result:
                print(f"{city} находится в стране {result}")
            else:
                print("Город не найден")
        elif auswahl == "0":
            break
        else:
            print("Ошибка ввода")
main()           