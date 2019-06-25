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

        self.city.calculate_year()
        self.city.calculate_price()
        self.city.workpower(food)

        self.city.calculate_acres(acres)
        self.city.calculate_harvest(plant)
        self.city.calculate_loss_by_rats()

        self.city.calculate_death_by_starving(food)
        self.city.calculate_death_by_illness()

        self.city.calculate_immigrants()
        self.city.calculate_population()

        self.game_over()
        self.view.setInfo()
        if self.city.gameover == True:
            print("Es ist vorbei")



    def new_game(self):
        print('new game method')








