import random
import math


##ADD THIS IN VIEW

#inputs
food = 2000
trade = 20
plant = 10

#needed vars

harvest = 500


#variables

class City:
    def __init__(self, population=100, city_name="Sumer", grain=1000, acres=1000, year=0, gameover=False, starved = 0, immigrants = 5, bushel_per_acre = 5, rats = 0, bushel = 2800, land_price = 21):
        self.population = population
        self.city_name = city_name
        self.grain = grain
        self.acres = acres
        self.year = year
        self.gameover = gameover
        self.starved = starved
        self.immigrants = immigrants
        self.bushel_per_acre = bushel_per_acre
        self.rats = rats
        self.bushel = bushel
        self.land_price = land_price
        self.food = food
        self.trade = trade
        self.plant = plant
        self.harvest = harvest
        self.workp = 0
        self.price = 0
        self.current = population

    def calculate_year(self):
        self.year += 1
        return self.year

    def calculate_price(self):
        self.price = random.randrange(17, 27)
        return int(self.price)

    def calculate_population(self):
        current = self.population
        starving = self.calculate_death_by_starving()
        illness = self.calculate_death_by_illness(starving)
        print("death by illness", illness)
        print("death by starving", starving)

        self.current = current
        self.population = current + self.immigrants - illness - starving
        print("current", self.current)
        print("population", self.population)

        return self.population


    def calculate_death_by_starving(self):
        self.starved = abs(math.trunc(int(self.population - (self.food / 20))))
        return self.starved


    def calculate_death_by_illness(self, starving):
        random_probability = random.randrange(0, 101)
        random_amount = random.randrange(0, (int((self.population - starving) * 0.25)))
        self.death_by_illness = math.trunc(int(random_amount * (random_probability / 100)))
        return self.death_by_illness

    def calculate_loss_by_rats(self,harvest):

        random_probability = random.randrange(0, 101)
        random_amount = random.randrange(0, (harvest * 0.25))
        self.loss_by_rats = math.trunc(int(random_amount * (random_probability / 100)))
        print("loss by rats",self.loss_by_rats)
        return self.loss_by_rats







    def workpower(self, food):
        productivity = int(food) / (self.population*20)
        if productivity > 1:
            productivity -= 1
        self.workp = self.population*productivity *10
        return self.workp



    def calculate_harvest(self, plant):
        random_crop = int(random.randrange(1,9))
        if self.workp < int(plant):
            self.harvest = random_crop * plant
        else:
            self.harvest = random_crop * plant * self.workp
        #print("harvest", self.harvest)
        return self.harvest

    def calculate_stock(self):

        self.stock = self.grain-self.food-self.plant-(self.trade*self.price)-self.loss_by_rats
        self.stock = self.stock + int(harvest)

        #print("stock",self.stock)
        return self.stock

# not working yet
    def calculate_immigrants(self, acres):

        if (self.stock/20) > self.population and self.workp < acres:
            self.immigrants = random.randrange(0, 10)
        else:
            self.immigrants = 0

        #print("immigrants calc", self.immigrants)
        return self.immigrants

    def sell_acres(self):
        self.acres += self.trade
        #print("acres", self.acres)
        return self.acres

    def gameover(self):
        """ outputs true or false"""

        #if year == 10

        pass

