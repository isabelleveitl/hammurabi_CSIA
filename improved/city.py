import random
import math


class City:
    def __init__(self, population=100, city_name="Sumer", grain=1000, acres=1000, year=0, gameover=False, starved = 0, immigrants = 5, bushel_per_acre = 5, rats = 0, bushel = 2800, price = 21):
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
        self.price = price
        self.trade = 20
        self.plant = 10
        self.harvest = 500
        self.workp = 0
        self.current = population
        self.sellAcres = 0
        self.buyAcres = 0
        self.loss_by_rats = 0
        self.death_by_illness = 0;

    def calculate_year(self):
        self.year += 1
        print("year", self.year)
        return self.year

    def calculate_price(self):
        self.price = random.randrange(17, 27)
        print("price",self.price)
        return self.price

    def workpower(self, food):
        productivity = int(food) / (self.population*20)
        if productivity > 1:
            productivity -= 1
        self.workp = self.population*productivity
        print("workpower",self.workp)
        return self.workp


    def calculate_harvest(self, plant):
        random_crop = random.randrange(1,9)
        if self.workp < int(plant):
            self.harvest = random_crop * int(plant)
        else:
            self.harvest = random_crop * int(plant) * self.workp
        print("harvest",self.harvest)

        self.bushel = self.bushel + self.harvest - int(plant)
        return self.harvest


    def calculate_loss_by_rats(self):
        random_probability = random.randrange(0, 101)
        random_amount = random.randrange(0, int(round(self.harvest * 0.25)))
        self.loss_by_rats = math.trunc(int(random_amount * (random_probability / 100)))
        print("loss by rats",self.loss_by_rats)
        self.bushel = self.bushel - self.loss_by_rats
        return self.loss_by_rats


    def calculate_death_by_starving(self, food):
        if self.population > int(food):
            self.starved = math.trunc(int(self.population - (int(food) / 20)))
        else:
            pass
        print("starving", self.starved)
        return self.starved


    def calculate_death_by_illness(self):
        random_probability = random.randrange(0, 101)
        if self.population > self.starved:
            calc = (self.population - self.starved) * 0.25
            random_amount = random.randrange(0, int(calc))
            self.death_by_illness = math.trunc(int(random_amount * (random_probability / 100)))
            print("deathIll",self.death_by_illness)
        else:
            pass
        return self.death_by_illness


    def calculate_acres(self, acres):
        ac = int(acres)
        self.acres = self.acres + ac
        if ac < 0:
            self.minusAcres(ac)
        else:
            self.plusAcres(ac)
        return self.acres

    def plusAcres(self, ac):
        self.bushel = self.bushel + (ac*self.price)

    def minusAcres(self, ac):
        self.bushel = self.bushel + (abs(ac)*self.price)


    def calculate_immigrants(self):
        if (self.bushel/20) > self.population and self.workp < self.acres:
            self.immigrants = random.randrange(0, 10)
        else:
            self.immigrants = 0
        print("immigrants calc", self.immigrants)
        return self.immigrants



    def calculate_population(self):
        current = self.population
        starving = self.starved
        illness = self.death_by_illness
        print("death by illness", illness)
        print("death by starving", starving)
        print("pre population", current)

        self.population = current + self.immigrants - illness - starving
        print("population", self.population)

        return self.population




    def gameover(self):
        """ outputs true or false"""

        #if year == 10

        pass

