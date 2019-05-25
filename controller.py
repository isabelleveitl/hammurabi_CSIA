class Controller:
    def __init__(self, city, view):
        self.city = city
        self.view = view
        self.view.set_listener(self.update_city)

    def start(self):
        self.view.show()

    def update_city(self, acres, food, plant):
        print('update city method with variables: ', acres, food, plant)


'''city = m.City()

print(city.population)
print(city.city_name)
print(city.grain)
print(city.acres)
print(city.year)'''

##update model



def new_game():
    print('new game method')

