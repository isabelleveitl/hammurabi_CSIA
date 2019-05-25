import unittest
from hammurabi_CSIA import city as ci

class TestCity(unittest.TestCase):
    def setUp(self):
        self.city = ci.City()

    #def test_calculate_loss_by_rats(self):
    #    result = self.city.calculate_loss_by_rats(200)
    #   self.assertLessEqual(result,200*0.25)

    def test_price(self):
        result = self.city.price()
        self.assertLessEqual(result,27)


