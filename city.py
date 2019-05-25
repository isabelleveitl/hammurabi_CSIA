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
    def __init__(self, population=100, city_name="Sumer", grain=1000, acres=100, year=0, gameover=False):
        self.population = population
        self.city_name = city_name
        self.grain = grain
        self.acres = acres
        self.year = year
        self.gameover = gameover

    def calculate_year(self):
        global year
        year += 1
        return year

    def price(self):
        """
        random price (grains) per year calculated between 17 & 26.
        :return: int
        """
        price = random.randrange(17, 27)
        return price

    def calculate_population(self):
        pass

    def calculate_loss_by_rats(self):
        """"amount of grains """

        random_probability = random.randrange(0, 101)
        random_amount = random.randrange(0, (harvest * 0.25))
        loss_by_rats = math.trunc(int(random_amount * (random_probability / 100)))
        print(loss_by_rats)

    def calculate_death_by_starving(self):
        """
        returns number of people who died from starving. minimum =0
        :return: int
        """
        global death_by_starving

        death_by_starving = math.trunc(int(city.population - (food / 20)))
        if death_by_starving < 0:
            death_by_starving = 0
        print(death_by_starving)

    def calculate_death_by_illness(self):
        """ Number of people who die - max a 25% share of the current population"""

        random_probability = random.randrange(0, 101)
        random_amount = random.randrange(0, ((self.population - death_by_starving) * 0.25))
        death_by_illness = math.trunc(int(random_amount * (random_probability / 100)))

        print(death_by_illness)

    def calculate_harvest(self):
        pass

    def workpower(self):
        pass

    def calculate_stock(self):
        pass

    def calculate_immigrants(self):
        pass

    def sell_acres(self):
        pass

    def gameover(self):
        """ outputs true or false"""

        #if year == 10

        pass




#business logic


city = City()

city.calculate_death_by_starving()
city.calculate_death_by_illness()
city.calculate_loss_by_rats()

