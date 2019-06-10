import unittest
import city as c

## run with: python -m unittest discover -s test

class TestCity(unittest.TestCase):

    def setUp(self):
        self.city = c.City()

    # test for correct construction of instance
    def test_construction(self):
        self.assertEqual(100, self.city.population)
        self.assertEqual(1000, self.city.grain)
        self.assertEqual(0, self.city.year)
        self.assertEqual(0, self.city.starved)
        self.assertEqual(5, self.city.immigrants)
        self.assertEqual(5, self.city.bushel_per_acre)
        self.assertEqual(0, self.city.rats)
        self.assertEqual(2800, self.city.bushel)
        self.assertEqual(21, self.city.land_price)
        self.assertFalse(self.city.gameover)
        self.assertNotEqual("", self.city.city_name)

    def test_calculate_year(self):
        self.assertEqual(self.city.year+1, self.city.calculate_year())

    def test_price(self):
        self.assertLess(16, self.city.price())
        self.assertGreater(27, self.city.price())

    def test_calculate_loss_by_rats(self):
        harvest = 500
        self.assertGreater(harvest, self.city.calculate_loss_by_rats(harvest))

    def test_calculate_death_by_starving(self):
        self.city.food = 2000
        self.city.population = 100
        self.assertEqual(0, self.city.calculate_death_by_starving())
        self.city.food = 10
        self.assertLess(0, self.city.calculate_death_by_starving())

    def test_calculate_death_by_illness(self):
        starving = 0
        self.assertGreater(self.city.population, self.city.calculate_death_by_illness(starving))
        starving = 120
        self.assertGreater(self.city.population, self.city.calculate_death_by_illness(starving))






