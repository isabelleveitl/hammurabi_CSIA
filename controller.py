class Controller:
    def __init__(self, city, view):
        self.city = city
        self.view = view

    def start(self):
        self.view.show()


'''city = m.City()

print(city.population)
print(city.city_name)
print(city.grain)
print(city.acres)
print(city.year)'''

##update model

def update_city(acres, food, plant):
    print('update city method with variables: ', acres, food, plant)

def new_game():
    print('new game method')

