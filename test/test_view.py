import unittest
import view as v
import city as c

## run with: python -m unittest discover -s test

class TestView(unittest.TestCase):

    def setUp(self):
        _city = c.City()
        self.view = v.View(_city)

    def test_call_listener(self):
        pass

    def test_set_text(self):
        self.assertIsNotNone(self.view.city.city_name)
        self.assertIsNotNone(self.view.city.starved)
        self.assertIsNotNone(self.view.city.population)
        self.assertIsNotNone(self.view.city.bushel_per_acre)
        self.assertIsNotNone(self.view.city.bushel)
        self.assertIsNotNone(self.view.city.rats)
        self.assertIsNotNone(self.view.city.acres)
        self.assertIsNotNone(self.view.city.land_price)







