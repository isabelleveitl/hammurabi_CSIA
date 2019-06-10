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

    def calculate_year(self):
        self.year += 1
        return self.year

    def price(self):
        """
        random price (grains) per year calculated between 17 & 26.
        :return: int
        """
        price = random.randrange(17, 27)
        return price

    def calculate_population(self):
        pass

    def calculate_loss_by_rats(self, harvest):
        """"amount of grains """

        random_probability = random.randrange(0, 101)
        random_amount = random.randrange(0, (harvest * 0.25))
        loss_by_rats = math.trunc(int(random_amount * (random_probability / 100)))
        return loss_by_rats

    def calculate_death_by_starving(self):
        """
        returns number of people who died from starving. minimum =0
        :return: int
        """
        death_by_starving = math.trunc(int(self.population - (self.food / 20)))
        print(death_by_starving)
        if death_by_starving < 0:
            death_by_starving = 0
        return death_by_starving

    def calculate_death_by_illness(self, death_by_starving):
        """ Number of people who die - max a 25% share of the current population"""

        random_probability = random.randrange(0, 101)
        random_amount = 0
        if death_by_starving < self.population:
            random_amount = random.randrange(0, (int((self.population - death_by_starving) * 0.25)))
        death_by_illness = math.trunc(int(random_amount * (random_probability / 100)))

        return death_by_illness

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
city.calculate_death_by_illness(1)
city.calculate_loss_by_rats(200)

