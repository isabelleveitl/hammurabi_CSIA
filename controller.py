class Controller:
    def __init__(self, city, view):
        self.city = city
        self.view = view
        self.view.set_listener(self.update_city)
        self.view.set_listener2(self.new_game)

    def start(self):
        self.view.show()

    def game_over(self):
        if self.city.year>=10:
            self.city.gameover = True
        elif (self.city.starved/self.city.population)>=0.45:
            self.city.gameover = True
        elif self.city.population==0:
            self.city.gameover = True
        else:
            self.city.gameover = False


    def update_city(self, acres, food, plant):
        self.city.calculate_price()
        self.city.calculate_harvest(self.city.plant)
        self.city.calculate_loss_by_rats(self.city.harvest)
        self.city.calculate_death_by_starving()
        self.city.calculate_death_by_illness()
        self.city.calculate_workpower(self.city.food)
        self.city.calculate_stock(self.city.land_price)
        self.city.calculate_immigrants()
        self.city.calculate_population()
        self.city.sell_acres(self.city.trade)
        self.city.calculate_year()
        self.game_over()
        if self.city.gameover == True:
            print("Es ist vorbei")




    def new_game(self):
        print('new game method')


'''city = m.City()

print(city.population)
print(city.city_name)
print(city.grain)
print(city.acres)
print(city.year)'''

##update model





