class Country:
    def __init__(self, name, cities):
        self.name = name
        self.cities = cities

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Название страны не должно быть пустым")
        self._name = value
    @property
    def cities(self):
        return self._cities
    @cities.setter
    def cities(self, value):
        if not isinstance(value, list):
            raise ValueError("Города должны быть списком")
        self._cities = value
    
    def __str__(self):
        return f"Страна {self.name}, города: {', '.join(self.cities)}"