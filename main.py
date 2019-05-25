import controller as c
import view as v
import city as city

ctrl = c.Controller(city.City(), v.View())
ctrl.start()