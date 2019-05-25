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


#business logic

def year():
    year +=1
    return year

def price():
    price = 1
    return price

def calculate_population():
    pass

def calculate_loss_by_rats():
    pass

def calculate_death_by_illness():
    pass

def calculate_death_by_starving():
    pass

def harvest():
    pass

def workpower():
    pass

def calculate_stock():
    pass

def calculate_immigrants():
    pass

def sell_acres():
    pass

def gameover():
    pass

