import csv, pickle
from country import Country

def save_to_csv(countries, filename):
    with open(filename, "w", newline = "", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Country", "City"])
        for country in countries:
            for city in country.cities:
                writer.writerow([country.name, city])

def load_from_csv(filename):
    data = {}
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)
        for country, city in reader:
            data.setdefault(country, []).append(city)
        return [Country(name, cities) for name, cities in data.items()]
    
def save_to_pickle(countries, filename):
    with open(filename, "wb") as file:
        pickle.dump(countries, file)
def load_from_pickle(filename):
    with open(filename, "rb") as file:
        return pickle.load(file)

