import unittest
import controller as c
import city as ci
import view as v

## run with: python -m unittest discover -s test

class TestController(unittest.TestCase):

    def setUp(self):
        city = ci.City()
        view = v.View(city)
        self.controller = c.Controller(city, view)

    def test_constructor(self):
        self.assertIsNotNone(self.controller.city)
        self.assertIsNotNone(self.controller.view)
