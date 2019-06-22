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
    def __init__(self, population=100, city_name="Sumer", grain=1000, acres=1000, year=0, gameover=False, starved = 0, immigrants = 5, bushel_per_acre = 5, rats = 0, bushel = 2800, land_price = 21, workpower = 0):
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
        self.workpower = workpower

    def calculate_year(self):
        self.year += 1
        return self.year

    def calculate_price(self):
        """
        random price (grains) per year calculated between 17 & 26.
        :return: int
        """
        self.land_price = random.randrange(17, 27)
        return(self.land_price)

    def calculate_population(self):
        self.population = self.population + self.immigrants - self.death_by_illness

        if self.death_by_starving > 0:
            self.population - self.death_by_starving

        return self.population

    def calculate_loss_by_rats(self,harvest):
        """"amount of grains """

        random_probability = random.randrange(0, 101)
        random_amount_stop = int(((self.harvest * 0.25)+1))
        random_amount = random.randrange(0, random_amount_stop)
        self.loss_by_rats = math.trunc(int(random_amount * (random_probability / 100)))
        return self.loss_by_rats

    def calculate_death_by_starving(self):
        """
        returns number of people who died from starving. minimum =0
        :return: int
        """
        self.death_by_starving = math.trunc(int(self.population - (food / 20)))
        if self.death_by_starving < 0:
            self.death_by_starving = 0
        return self.death_by_starving


    def calculate_death_by_illness(self):
        """ Number of people who die - max a 25% share of the current population"""

        random_probability = random.randrange(0, 101)
        random_amount = random.randrange(0, (int((self.population - self.death_by_starving) * 0.25)))
        self.death_by_illness = math.trunc(int(random_amount * (random_probability / 100)))

        return self.death_by_illness


    def calculate_workpower(self,food):

        productivity = food /(self.population*20)
        if productivity > 1:
            productivity -= 1
        self.workpower = self.population*productivity *10

        return self.workpower

    def calculate_harvest(self, plant):
        random_crop = random.randrange(1,9)

        if self.workpower < plant:
            self.harvest = random_crop * plant
        else:
            self.harvest = random_crop * plant* self.workpower
        return self.harvest

    def calculate_stock(self, land_price):
        self.stock = self.grain-food-plant-(trade*self.land_price)-self.loss_by_rats+self.harvest
        return self.stock

    def calculate_immigrants(self):

        if (self.stock/20) > self.population and self.workpower < self.acres:
            self.immigrants = random.randrange(0, 10)
        else:
            self.immigrants = 0
        return self.immigrants

    def sell_acres(self, trade):
        self.acres += trade
        return self.acres

    def gameover(self):
        """ outputs true or false"""

        #if year == 10

        pass




#funktionen ausführen - test

city = City()

city.calculate_death_by_starving()
city.calculate_death_by_illness()
city.calculate_harvest(500)
print(city.harvest)
city.calculate_loss_by_rats(city.harvest)
print(city.loss_by_rats)
city.calculate_workpower(3000)
city.calculate_stock(5)
city.calculate_immigrants()
city.sell_acres(-20)
city.calculate_population()